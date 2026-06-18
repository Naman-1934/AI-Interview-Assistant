from src.speech_analyzer.whisper_transcriber import transcribe_audio
from src.answer_evaluator.answer_evaluator import evaluator_answer
from src.database.db import save_result



def run_interview(questions, candidate_answers):
    results = []

    for q, answer in zip(questions, candidate_answers):

        evaluation = evaluator_answer(question=q["question"], expected_answer=q["expected_answer"], candidate_answer=answer)

        save_result(question=q["question"], expected_answer=q["expected_answer"], candidate_answer=answer, evaluation=evaluation)

        results.append({"question": q["question"], "evaluation": evaluation})

    return results  

        