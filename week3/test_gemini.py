
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found!")
    raise SystemExit

try:
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(timeout=120000)
    )

    print("Testing Gemini 3.6 Flash...")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="What is Artificial Intelligence? Explain in 2 lines."
    )

    print("\nGemini Response:")
    print(response.text)

    print("\nGemini API is working!")

except Exception as error:
    print("\nGemini API Error:")
    print(type(error).__name__)
    print(error)
