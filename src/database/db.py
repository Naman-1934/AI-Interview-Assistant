import sqlite3

import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_DB_PATH = os.path.join(_HERE, "..", "..", "Interview.db")

def create_connection():
    conn = sqlite3.connect(_DB_PATH)
    return conn

def create_table():
    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS interview_results(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            expected_answer TEXT,
            candidate_answer TEXT,
            technical_score REAL,
            correctness_score REAL,
            communication_score REAL,
            overall_score REAL,
            feedback TEXT
        )
        """
    )

    conn.commit()
    conn.close()

def save_result(question, expected_answer, candidate_answer, evaluation):
    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO interview_results(
        question,
        expected_answer,
        candidate_answer,
        technical_score,
        correctness_score,
        communication_score,
        overall_score,
        feedback
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            question,
            expected_answer,
            candidate_answer,
            evaluation["technical_score"],
            evaluation["correctness_score"],
            evaluation["communication_score"],
            evaluation["overall_score"],
            evaluation["feedback"]
        )
    )

    conn.commit()
    conn.close()