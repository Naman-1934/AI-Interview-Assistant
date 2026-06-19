import streamlit as st 
from src.resume_parser.resume_parser import parse_resume
from src.skill_extractor.skill_extractor import extract_skills
from src.profile_builder.profile_builders import detect_role
import tempfile
import os

st.set_page_config(page_title="Upload Resume", page_icon="📄", layout="wide")

st.title("📄 Upload your Resume")

uploaded_files = st.file_uploader("Upload your resume in PDF format", type=["pdf"])

if uploaded_files is not None:
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_files.read())
        tmp_path = tmp.name

    with st.spinner("Parsing your resume..."):
        text = parse_resume(tmp_path)

    with st.spinner("Extracting Skills..."):
        skills = extract_skills(text)

    with st.spinner("Detecting your role..."):
        profile = detect_role(skills)

    os.unlink(tmp_path)

    st.success("Resume Processed Successfully!")

    st.subheader("Detected Role")
    st.write(F"*** {profile['role']}** - Confidence: {profile['confidence'] * 100:.0f}% ")

    st.subheader("Extracted Skills")
    st.write(", ".join(skills))

    st.session_state["role"] = profile["role"]
    st.session_state["skills"] = skills

    st.info("Role and skills saved. Go to the Interview page to start.")