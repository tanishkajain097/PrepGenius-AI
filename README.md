# 🎓 PrepGenius AI – Intelligent Study Mentor Agent

PrepGenius AI is an AI-powered study mentor designed to help students learn more effectively through personalized and interactive learning support.

The application provides AI-based doubt solving, notes generation, quiz generation, personalized study planning, and flashcard generation through an easy-to-use Streamlit interface.

## 🚀 Live Demo

👉 https://prepgenius-ai-5bf4ntj3dqs3flkbvcftop.streamlit.app/

## ✨ Features

### 💡 Doubt Solver
Get clear and easy-to-understand explanations for academic questions and concepts.

### 📝 Notes Generator
Generate concise and structured study notes with headings and bullet points.

### ❓ Quiz Generator
Generate multiple-choice questions with answers for effective exam preparation.

### 📅 Study Planner
Create a personalized study plan based on the number of days remaining before an exam and available study hours per day.

### 🧠 Flashcard Generator
Generate question-and-answer style flashcards for quick revision and memorization.

## 🎯 Objectives

- Provide personalized learning assistance
- Help students resolve academic doubts
- Automate the creation of study materials
- Support effective exam preparation
- Make learning more interactive and accessible
- Improve learning efficiency through AI-powered assistance

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **AI API:** Groq API
- **AI Model:** OpenAI GPT-OSS-20B
- **Version Control:** Git & GitHub
- **Environment Management:** Python-dotenv

## ⚙️ How It Works

1. The user selects a learning task from the sidebar.
2. The user enters a topic or question.
3. For the Study Planner, the user provides the number of days until the exam and available study hours per day.
4. PrepGenius AI generates an appropriate prompt based on the selected task.
5. The prompt is sent to the AI model through the Groq API.
6. The generated response is displayed instantly in the Streamlit application.

## 📂 Project Structure

```text
PrepGenius-AI/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
