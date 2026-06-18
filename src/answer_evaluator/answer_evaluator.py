import json
import time
from src.gemini.config import client

def evaluator_answer(question, expected_answer, candidate_answer, retries=3, delay=5):

    prompt = f"""
You are an expert technical interviewer.

Question:
{question}

Expected Answer:
{expected_answer}

Candidate Answer
{candidate_answer}

Evaluate the answer.

Provide:

1. Technical Score (0-10)
2. Correctness Score (0-10)
3. Communication Score (0-10)
4. Overall Score (0-10)
5. Detailed Feedback

Return valid JSON only.

Format:

{{
    "technical_score": 0,
    "correctness_score": 0,
    "communication_score": 0,
    "overall_score": 0,
    "feedback": ""
}}
"""
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt
            )
            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(clean_text)

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)

    raise RuntimeError("Gemini API failed after all retries.")