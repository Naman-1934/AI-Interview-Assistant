import streamlit as st
from src.gemini.question_generator import generate_questions
from src.speech_analyzer.reccord_audio import record_audio
from src.speech_analyzer.whisper_transcriber import transcribe_audio
from src.answer_evaluator.answer_evaluator import evaluator_answer
from src.database.db import create_table, save_result

st.set_page_config(page_title="Interview Session", page_icon="🎤", layout="wide")

st.title("🎤 Interview Session")


# create_table() is called here to make sure the database table exists before we try to save anything
create_table()

# We check st.session_state, If role and skills aren't there it means the user skipped Page 1, 
# so we warn them and call st.stop() which stops the page from running further
if "role" not in st.session_state or "skills" not in st.session_state:
    st.warning("Please upload your resume first on the Upload Resume Page")
    st.stop()

role = st.session_state["role"]
skills = st.session_state["skills"]

st.write(f"** Role:** {role}")
st.write(f"** Skills:** {', '.join(skills)}")

if "questions" not in st.session_state:
    with st.spinner("Generating interview questions..."):
        import json
        raw = generate_questions(role=role, skills=skills, num_questions=15)
        st.session_state["questions"] = json.loads(raw)


# We store questions in st.session_state["questions"] so they don't get regenerated every time the page refreshes, because
# Streamlit reruns the entire script on every button click
questions = st.session_state["questions"]

# st.session_state["current_question"] tracks which question the user is on across reruns
if "current_question" not in st.session_state:
    st.session_state["current_question"] = 0

if "interview_done" not in st.session_state:
    st.session_state["interview_donw"] = False

if not st.session_state["interview_done"]:
    idx = st.session_state["current_question"]

    if idx < len(questions):
        q = questions(idx)

        st.subheader(f"Question {idx + 1} of {len(questions)}")
        st.write(f"** {q['question']}**")
        st.caption(f"Difficulty: {q['difficulty']}")

        # st.slider() lets the user choose how many seconds to record because some answers need more time than others
        duration = st.slider("Recording duration (seconds)", 5, 30, 10)

        if st.button("🎙️ Record My Answer"):

            with st.spinner(f"Recording for {duration} seconds..."):
                audio_file = record_audio(filename="answer.wav", duration=duration)

            st.success("Recording Done!")

            with st.spinner("Transcribing your answer"):
                candidate_answer = transcribe_audio(audio_file)

            st.write("**Your Answer:**", candidate_answer)

            with st.spinner("Evaluating your answer"):
                evaluation = evaluator_answer(
                    question=q["question"],
                    expected_answer=q.get("expected_answer", ""),
                    candidate_answer=candidate_answer
                )

            save_result(
                question=q["question"],
                expected_answer=q.get("expected_answer", ""),
                candidate_answer=candidate_answer,
                evaluation=evaluation
            )

            # st.columns(4) splits the scores into 4 side by side boxes — cleaner than listing them vertically
            st.write("**Scores**")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Technical", f"{evaluation['technical_score']} / 10")
            col2.metric("Correctness", f"{evaluation['correctness_score']} / 10")
            col3.metric("Communication", f"{evaluation['communication_score']} /10")
            col4.metric("Overall", f"{evaluation['overall_score']} /10")

            st.write("**Feedback:**", evaluation['feedback'])

            st.session_state['current_question'] += 1

            if st.session_state["current_question"] >= len(questions):
                st.session_state["interview_done"] = True

                # st.rerun() forces Streamlit to rerun the page immediately after saving, 
                # this moves the user to the next question automatically
                st.rerun()
            else:
                st.rerun()

else:
    st.success("🎉 Interview Complete! Go to the Scorecard page to see your results.")
            

