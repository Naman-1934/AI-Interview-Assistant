import streamlit as st
import sqlite3
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(page_title="Scorecard", page_icon="📊", layout="wide")

st.title("📊 Interview Scorecard")

_HERE = os.path.dirname(os.path.abspath(__file__))
_DB_PATH = os.path.join(_HERE, "..", "interview.db")

conn = sqlite3.connect(_DB_PATH)

df = pd.read_sql_query("SELECT * FROM interview_results", conn)

conn.close()

if df.empty:
    st.warning("No interview results found. Please complete an interview first.")
    st.stop()

st.subheader("Overall Performance")

avg_technical = df["technical_score"].mean()
avg_correctness = df["correctness_score"].mean()
avg_communication = df["communication_score"].mean()
avg_overall = df["overall_score"].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Technical", f"{avg_technical:.1f}/10")
col1.metric("Avg Correctness", f"{avg_correctness:.1f}/10")
col1.metric("Avg Communication", f"{avg_communication:.1f}/10")
col1.metric("Avg Overall", f"{avg_technical:.1f}/10")

st.subheader("Scores Per Question")

fig = go.figure()

fig.add_trace(go.Bar(
    name = "Technical",
    x = [f"Q{i+1}" for i in range(len(df))],
    y = df["technical_score"]
))

fig.add_trace(go.Bar(
    name = "Correctness",
    x = [f"Q{i+1}" for i in range(len(df))],
    y = df["correctness_score"]
))

fig.add_trace(go.Bar(
    name = "Communication",
    x = [f"Q{i+1}" for i in range(len(df))],
    y = df["Communication"]
))

fig.update_layout(
    barmode = "group",
    xaxis_title = "Questions",
    yaxis_title = "Score (Out of 10)",
    yaxis=dict(range=[0, 10])
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Overall Score Gauge")
gauge = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = avg_overall,
    gauge={
        "axis": {"range": [0, 10]},
        "bar": {"color": "green"},
        "steps": [
            {"range": [0,4], "color": "red"},
            {"range": [4,7], "color": "orange"},
            {"range": [7,10], "color": "lightgreen"},

        ]
    },
    title = {"text": "Overall Score"}
))

st.plotly_chart(gauge, use_container_width=True)

st.subheader("Detailed Feedback Per Question")

for i, row in df.iterrows():
    with st.expander(f"Q{i+1}: {row['question'][:80]}..."):
        st.write("**Your Answer:**", row["candidate_answer"])
        st.write("**Feedback:**", row["feedback"])
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Technical", f"{row['technical_score']}/10")
        col2.metric("Correctness", f"{row['correctness_score']}/10")
        col3.metric("Communication", f"{row['communication_score']}/10")
        col4.metric("Overall", f"{row['overall_score']}/10")
