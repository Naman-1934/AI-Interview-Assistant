# from answer_evaluator import evaluator_answer

# result = evaluator_answer(

#     question = "What is a decorator in Python?",

#     expected_answer = "A decorator is a function that modifies another function without changing its source code.",

#     candidate_answer = "Decorator is used to add functionality to a function without modifying the original function."
# )

# print(result)

from google import genai

API_KEY = None

print("CONFIG FILE LOADED")

client = genai.Client(
    api_key="AQ.Ab8RN6IXwHGBcZ71A4UWy6jcRRL0uVQbzx9m1NBaJlw8lXnU9g"
)