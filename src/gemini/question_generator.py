from config import model
import json


def generate_questions(
        role,
        skills,
        num_questions = 15
):
    
    prompt = f"""
You are an expert technical interviewer and ask questions from easy to difficult level.

Role:
{role}

Skills:
{', '.join(skills)}

Generate {num_questions} interview questions.

Mix:

Easy 
Medium
Hard

Generate:
6 Easy Questions

6 Medium Questions

3 Hard Questions

Return JSON Only.
Do not use markdown.
Do not use code fences.

Format:

[
 {{
    "question":"",
    "difficulty":"" 
 }}
]
"""
    response = model.generate_content(
        prompt
    )

    return response.text