
import os
import time
import re
import requests

from dataclasses import dataclass
from abc import ABC, abstractmethod

from google import genai
from google.genai import types


# Common LLM Result
@dataclass
class LLMResult:
    text: str
    input_tokens: int = 0
    output_tokens: int = 0


# Abstract Provider
class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


# Gemini Provider
class GeminiProvider(LLMProvider):

    provider_name = "Gemini"

    def __init__(self, api_key, model="gemini-3.6-flash"):

        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing!")

        self.model = model

        self.client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(
                timeout=120000
            )
        )

    def generate(self, prompt):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        usage = response.usage_metadata

        input_count = getattr(
            usage, "prompt_token_count", 0
        ) or 0

        output_count = getattr(
            usage, "candidates_token_count", 0
        ) or 0

        return LLMResult(
            text=response.text or "",
            input_tokens=input_count,
            output_tokens=output_count
        )


# Ollama Provider
class OllamaProvider(LLMProvider):

    provider_name = "Ollama"

    def __init__(self, model="llama3.2"):

        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=(5, 120)
        )

        response.raise_for_status()

        data = response.json()

        return LLMResult(
            text=data.get("response", ""),
            input_tokens=data.get("prompt_eval_count", 0) or 0,
            output_tokens=data.get("eval_count", 0) or 0
        )


# Common LLM Client
class LLMClient:

    def __init__(self, provider, usage_logger):

        self.provider = provider
        self.usage_logger = usage_logger

    # Save usage details
    def save_usage(self, data):

        try:
            if self.usage_logger:
                self.usage_logger.log_call(data)

        except Exception as error:
            print("MongoDB logging error:", error)

    # Check temporary errors
    def is_retryable(self, error):

        status = getattr(error, "status_code", None)

        if status is None:
            status = getattr(error, "code", None)

        message = str(error).lower()

        retry_codes = (408, 429, 500, 502, 503, 504)

        if status in retry_codes:
            return True

        retry_messages = [
            "deadline_exceeded",
            "resource_exhausted",
            "temporarily unavailable",
            "service unavailable",
            "timeout",
            "connection reset",
            "connection error",
            "504",
            "503",
            "429"
        ]

        return any(item in message for item in retry_messages)

    # Generate response
    def generate(self, prompt):

        start = time.perf_counter()
        max_attempts = 3

        input_rate = float(os.getenv(
            "GEMINI_INPUT_PRICE_PER_MILLION", "0"
        ))

        output_rate = float(os.getenv(
            "GEMINI_OUTPUT_PRICE_PER_MILLION", "0"
        ))

        for attempt in range(max_attempts):

            try:

                result = self.provider.generate(prompt)

                latency_ms = round(
                    (time.perf_counter() - start) * 1000, 2
                )

                # Calculate cost
                if self.provider.provider_name == "Gemini":

                    cost = (
                        result.input_tokens * input_rate
                        + result.output_tokens * output_rate
                    ) / 1_000_000

                    cost_type = "estimated_hosted_api_cost"

                else:

                    cost = 0.0
                    cost_type = "local_inference_cost_not_included"

                # Save successful usage
                usage_data = {

                    "provider": self.provider.provider_name,
                    "model": self.provider.model,

                    "input_tokens": result.input_tokens,
                    "output_tokens": result.output_tokens,

                    "total_tokens": (
                        result.input_tokens + result.output_tokens
                    ),

                    "latency_ms": latency_ms,
                    "estimated_cost_usd": round(cost, 8),
                    "cost_type": cost_type,

                    "status": "success",
                    "attempts": attempt + 1

                }

                self.save_usage(usage_data)

                # Display successful result
                print("\nRequest Successful!")

                print("Latency:", latency_ms, "ms")
                print("Input tokens:", result.input_tokens)
                print("Output tokens:", result.output_tokens)

                print(
                    "Total tokens:",
                    result.input_tokens + result.output_tokens
                )

                print("Estimated cost (USD):", round(cost, 8))

                return result.text

            except Exception as error:

                latency_ms = round(
                    (time.perf_counter() - start) * 1000, 2
                )

                retryable = self.is_retryable(error)

                # Stop if permanent error or final attempt
                if not retryable or attempt == max_attempts - 1:

                    self.save_usage({

                        "provider": self.provider.provider_name,
                        "model": self.provider.model,

                        "input_tokens": None,
                        "output_tokens": None,
                        "total_tokens": None,

                        "latency_ms": latency_ms,
                        "estimated_cost_usd": None,

                        "status": "failed",
                        "attempts": attempt + 1,
                        "error": str(error)

                    })

                    print("\nLLM Request Failed!")
                    print("Error:", error)

                    return None

                # Retry temporary errors
                delay = 2 ** (attempt + 1)

                print(
                    f"Temporary error. Retry "
                    f"{attempt + 1} of {max_attempts - 1} "
                    f"in {delay} seconds."
                )

                time.sleep(delay)
