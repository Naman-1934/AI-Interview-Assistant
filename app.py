import streamlit as st
from src.ui.layout import inject_base_css, render_navbar, nav_buttons

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_base_css()
render_navbar("home")

st.markdown('<div class="app-card">', unsafe_allow_html=True)

st.markdown('<div class="eyebrow">AI-Powered Mock Interviews</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Practice interviews that actually evaluate you</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-sub">Upload your resume, answer real questions out loud, and get an '
    'AI-scored breakdown of your technical depth, correctness, and communication.</div>',
    unsafe_allow_html=True
)

st.write("")

steps_data = [
    ("01", "Upload Resume", "We extract your skills and detect your role automatically."),
    ("02", "Interview Session", "Answer questions out loud. AI evaluates each response live."),
    ("03", "Scorecard", "See your scores, feedback, and where to improve."),
]

cols = st.columns(3)
for col, (num, title, desc) in zip(cols, steps_data):
    with col:
        st.markdown(f"""
        <div class="step-card">
            <div class="step-num">{num}</div>
            <div class="step-title">{title}</div>
            <div class="step-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<hr style="border-color: #262C3B; margin: 28px 0 20px 0;">', unsafe_allow_html=True)
nav_buttons("home")

st.markdown('</div>', unsafe_allow_html=True)