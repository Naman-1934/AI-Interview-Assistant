from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key = "AQ.Ab8RN6IKq3aCOYFW-FQMsI079aXo2xeI7-lE8-3_Lg7OKU4d0w"
)

MODEL_NAME = "gemini-2.5-flash"

prompt = """
Generate 15 Python interview questions.
"""

MAX_RETRIES = 15

for attempt in range(MAX_RETRIES):
    try:

        response = client.models.generate_content(
            model = MODEL_NAME,
            contents = prompt
        )

        print("\nResponse:\n")

        print(response.text)

        break

    except Exception as e:
        print(
            f"Attempt {attempt+1} failed"

        )

        print(e)

        time.sleep(5)

