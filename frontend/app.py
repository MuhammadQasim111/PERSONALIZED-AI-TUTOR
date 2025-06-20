import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agent.question_agent import generate_question
st.set_page_config(page_title="AI Math Quiz for Kids", layout="centered")
st.title("🎓 AI Math Quiz for Kids")

TOPICS = [
    "Pocket money",
    "School cafeteria",
    "Birthday party",
    "Toy shopping",
    "Homework planning"
]

selected_topic = st.selectbox("Choose a topic:", TOPICS)

if st.button("Generate Question"):
    question_data = generate_question(selected_topic)
    if question_data and not question_data.get("error"):
        st.session_state.question = question_data["question"]
        st.session_state.options = question_data["options"]
        st.session_state.correct_answer = question_data["correct"].strip().upper()
        st.session_state.explanation = question_data["explanation"]
        st.session_state.answered = False
    else:
        st.error(f"Failed to generate a valid question.\n{question_data.get('error', '')}")
        st.session_state.question = None

if st.session_state.get("question"):
    st.write(f"**Question:** {st.session_state.question}")
    answer = st.radio("Choose your answer:", st.session_state.options, key="answer_radio")

    if st.button("Submit Answer") and not st.session_state.get("answered", False):
        # Find the selected letter (A/B/C/D) based on index
        selected_index = st.session_state.options.index(answer)
        selected_letter = chr(65 + selected_index)  # 65 = 'A'
        if selected_letter == st.session_state.correct_answer:
            st.success("Correct! 🎉")
        else:
            st.error("Oops! That's not correct.")
        st.info(f"Explanation: {st.session_state.explanation}")
        st.session_state.answered = True
