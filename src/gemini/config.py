from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

print("API KEY:", API_KEY)

client = genai.Client(
    api_key="AQ.Ab8RN6IXwHGBcZ71A4UWy6jcRRL0uVQbzx9m1NBaJlw8lXnU9g"
)