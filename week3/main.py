
import os
from dotenv import load_dotenv

from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)

from usage_logger import UsageLogger


# Load environment variables
load_dotenv(override=True)


# Initialize MongoDB logger
usage_logger = UsageLogger()


try:

    print("\n===== WEEK 3 LLM APPLICATION =====")

    # Select provider
    provider_name = input(
        "Choose provider (gemini/ollama): "
    ).strip().lower()

    # Gemini provider
    if provider_name == "gemini":

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "Gemini API key not found in .env file!"
            )

        provider = GeminiProvider(
            api_key=api_key,
            model="gemini-3.6-flash"
        )

    # Ollama provider
    elif provider_name == "ollama":

        provider = OllamaProvider(
            model="llama3.2"
        )

    else:

        raise ValueError(
            "Invalid provider! Choose gemini or ollama."
        )

    # Create LLM client
    client = LLMClient(
        provider,
        usage_logger
    )

    # Get user question
    prompt = input("\nEnter your question: ").strip()

    if not prompt:
        raise ValueError("Question cannot be empty!")

    # Generate response
    answer = client.generate(prompt)

    # Display response
    if answer:

        print("\n========== LLM RESPONSE ==========")
        print(answer)
        print("==================================")

    else:

        print("\nNo response generated. Please try again.")

except ValueError as error:

    print("\nInput Error:", error)

except KeyboardInterrupt:

    print("\nProgram stopped by user.")

except Exception as error:

    print("\nApplication Error:", error)

finally:

    usage_logger.close()

    print("\nMongoDB connection closed.")
    print("Program completed.")
