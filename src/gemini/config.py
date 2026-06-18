from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key="AQ.Ab8RN6IKq3aCOYFW-FQMsI079aXo2xeI7-lE8-3_Lg7OKU4d0w")