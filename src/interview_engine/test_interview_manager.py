# src/interview_engine/test_interview_manager.py

from src.interview_engine.interview_manager import run_interview

def test_run_interview():
    questions = [
        {
            "question": "What is a decorator?",
            "expected_answer": "A decorator modifies another function."
        },
        {
            "question": "What is a list?",
            "expected_answer": "Mutable collection in python."
        }
    ]

    candidate_answers = ["Decorator modifies another function", "List is mutable"]

    results = run_interview(questions, candidate_answers)

    assert isinstance(results, list)
    assert len(results) == 2
    assert "evaluation" in results[0]
    print(results)