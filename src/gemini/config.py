from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key="AQ.Ab8RN6ItUeTEUqfcIpM70Y4WgPoDbyZNytUqozXbpIOWWHzh7A")
