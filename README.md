# 📖 Smart Student Assistant

An intelligent, terminal-based chatbot designed to help students with study-related queries.This assistant uses the Gemini 1.5 Flash model via the Google Generative AI API and responds to academic questions in a conversational way.

---
## 🚀 Features

🤖 Responds to study-related queries using Gemini AI

📚 Helps with explanations, summaries, and study tips

⛔️ Ignores or filters out unrelated topics

✅ Simple command-line interface (CLI)

🔐 Environment-safe with .env support

---
## 💠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/hassannawaz02/Smart-Student-Assistant.git

cd smart-student-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```
### 3. Add your .env file

```bash
Create a file named .env and add your Google Gemini API key:

GEMINI_API_KEY=your_api_key_here
```
### 4. Run the Assistant

```bash
python main.py
```
---
## 🧠 How it Works

The assistant reads your input, detects if it’s an academic question, and sends it to Google Gemini's gemini-1.5-flash model.If your question is off-topic, the assistant politely reminds you that it's only for learning-related help.

---
## 🤝 Contribution

Feel free to fork and improve the assistant with more features like:

---

## 📜 License

This project is licensed under the MIT License.

---
“Stay curious. Keep learning. Help others do the same.” 😊📘

