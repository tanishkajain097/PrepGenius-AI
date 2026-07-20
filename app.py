import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
client=Groq(api_key=api_key)

st.set_page_config(page_title="PrepGenius AI",page_icon="🎓",layout="wide")
st.title("🎓 PrepGenius AI – Intelligent Study Mentor Agent")
st.caption("SDG 4 • Quality Education")

task=st.sidebar.selectbox("Choose Task",[
    "Doubt Solver","Notes Generator","Quiz Generator","Study Planner","Flashcard Generator"
])

topic=st.text_input("Enter Topic / Question")
days=None
hours=None
if task=="Study Planner":
    days=st.number_input("Days until exam",1,60,7)
    hours=st.number_input("Study hours/day",1,12,2)

def prompt():
    if task=="Doubt Solver":
        return f"Explain clearly with examples:\n{topic}"
    if task=="Notes Generator":
        return f"Create concise study notes with headings and bullets on: {topic}"
    if task=="Quiz Generator":
        return f"Create 10 MCQs with answers on: {topic}"
    if task=="Flashcard Generator":
        return f"Create 15 flashcards (Front: Back:) for: {topic}"
    return f"Create a {days}-day study plan for {topic} assuming {hours} hours/day."

if st.button("Generate"):
    if not api_key:
        st.error("API key missing. Add GROQ_API_KEY to .env")
    elif not topic:
        st.warning("Enter a topic first.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt()
                        }
                    ],
                    temperature=0.5
                )

                st.success("Done!")
                st.markdown(response.choices[0].message.content)

            except Exception as e:
                st.error(str(e))

st.markdown("---")
st.markdown("**Tech Stack:** Python • Streamlit • Groq API • Llama 3.3")