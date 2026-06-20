import streamlit as st
from src.resume_parser.resume_parser import parse_resume
from src.skill_extractor.skill_extractor import extract_skills
from src.profile_builder.profile_builders import detect_role
from src.ui.layout import inject_base_css, render_navbar, nav_buttons
import tempfile
import os

st.set_page_config(page_title="Upload Resume", page_icon="📄", layout="wide", initial_sidebar_state="collapsed")

inject_base_css()
render_navbar("resume")

st.markdown('<div class="app-card">', unsafe_allow_html=True)

st.title("📄 Upload Your Resume")

uploaded_file = st.file_uploader("Upload your resume in PDF format", type=["pdf"])

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("Parsing your resume..."):
        text = parse_resume(tmp_path)

    with st.spinner("Extracting skills..."):
        skills = extract_skills(text)

    with st.spinner("Detecting your role..."):
        profile = detect_role(skills)

    os.unlink(tmp_path)

    st.success("Resume processed successfully!")

    st.subheader("Detected Role")
    st.write(f"**{profile['role']}** — Confidence: {profile['confidence'] * 100:.0f}%")

    st.subheader("Extracted Skills")
    st.write(", ".join(skills))

    st.session_state["role"] = profile["role"]
    st.session_state["skills"] = skills

    st.info("✅ Role and skills saved. Go to the Interview page to start.")

st.write("")
st.markdown('<hr style="border-color: #262C3B; margin: 20px 0;">', unsafe_allow_html=True)
nav_buttons("resume")

st.markdown('</div>', unsafe_allow_html=True)