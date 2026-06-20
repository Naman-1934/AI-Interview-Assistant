import streamlit as st
from src.gemini.question_generator import generate_questions
from src.speech_analyzer.record_audio import record_audio
from src.speech_analyzer.whisper_transcriber import transcribe_audio
from src.answer_evaluator.answer_evaluator import evaluator_answer
from src.database.db import create_table, save_result
from src.ui.layout import inject_base_css, render_navbar, nav_buttons

st.set_page_config(page_title="Interview Session", page_icon="🎤", layout="wide", initial_sidebar_state="collapsed")

inject_base_css()
render_navbar("interview")

st.markdown('<div class="app-card">', unsafe_allow_html=True)

st.title("🎤 Interview Session")

create_table()

if "role" not in st.session_state or "skills" not in st.session_state:
    st.warning("Please upload your resume first on the Upload Resume page.")
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

role = st.session_state["role"]
skills = st.session_state["skills"]

st.write(f"**Role:** {role}")
st.write(f"**Skills:** {', '.join(skills)}")

if "questions" not in st.session_state:
    with st.spinner("Generating interview questions..."):
        import json
        raw = generate_questions(role=role, skills=skills, num_questions=15)
        st.session_state["questions"] = json.loads(raw)

questions = st.session_state["questions"]

if "current_question" not in st.session_state:
    st.session_state["current_question"] = 0

if "interview_done" not in st.session_state:
    st.session_state["interview_done"] = False

if not st.session_state["interview_done"]:

    idx = st.session_state["current_question"]

    if idx < len(questions):

        q = questions[idx]

        st.subheader(f"Question {idx + 1} of {len(questions)}")
        st.write(f"**{q['question']}**")
        st.caption(f"Difficulty: {q['difficulty']}")

        duration = st.slider("Recording duration (seconds)", 5, 30, 10)

        if st.button("🎙️ Record My Answer"):

            with st.spinner(f"Recording for {duration} seconds..."):
                audio_file = record_audio(filename="answer.wav", duration=duration)

            st.success("Recording done!")

            with st.spinner("Transcribing your answer..."):
                candidate_answer = transcribe_audio(audio_file)

            st.write("**Your Answer:**", candidate_answer)

            with st.spinner("Evaluating your answer..."):
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

            st.write("**Scores:**")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Technical", f"{evaluation['technical_score']}/10")
            col2.metric("Correctness", f"{evaluation['correctness_score']}/10")
            col3.metric("Communication", f"{evaluation['communication_score']}/10")
            col4.metric("Overall", f"{evaluation['overall_score']}/10")

            st.write("**Feedback:**", evaluation["feedback"])

            st.session_state["current_question"] += 1

            if st.session_state["current_question"] >= len(questions):
                st.session_state["interview_done"] = True
                st.rerun()
            else:
                st.rerun()

else:
    st.success("🎉 Interview Complete! Go to the Scorecard page to see your results.")
    st.write("")
    st.markdown('<hr style="border-color: #262C3B; margin: 20px 0;">', unsafe_allow_html=True)
    nav_buttons("interview")

st.markdown('</div>', unsafe_allow_html=True)