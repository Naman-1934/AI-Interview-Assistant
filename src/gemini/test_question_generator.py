from question_generator import generate_questions

questions = generate_questions(
    role = "Data Analyst",

    skills = [
        "python",
        "excel",
        "mysql",
        "power bi",
        "tableau"
    ],

    num_questions = 15
)

print(questions)