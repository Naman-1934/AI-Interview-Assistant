# This page is just a welcome screen — it explains the app to the user before they start


import streamlit as st

# set_page_config() must be the very first Streamlit call in any file — it sets the browser tab title, icon and layout
st.set_page_config(
    page_title = "AI Interview Assistant",
    page_icon= "🤖",

    # layout="wide" uses the full screen width instead of a narrow centered column
    layout= "wide"
)

st.title("🤖 AI Interview Assistant")

st.markdown("""
Welcome to your personal AI Interview Assistant
            
### How it Works:
1. Upload Resume = Upload your pdf resume. We extract your skills and detect your role automatically.
2. Interview Session = Answer questions out loud. AI evaluates your answers in real time.
3. Scorecard = See your score, feedback and areas to improve.
            
👈 Use sidebar to navigate between pages.
""")