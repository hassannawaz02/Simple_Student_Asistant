import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Set behavior
instructions = (
    "You are a Smart Student Assistant. Your role is to assist only with academic, educational, or study-related topics.\n"
    "If the query is unrelated, kindly respond with: \"I'm here to support academic learning only. 📘😊\""
)

# Welcome banner
print("📖✨ Welcome to the Smart Student Assistant ✨📖")
print("💡 Ask me about any subject, study tip, explanation, or summary help.")
print("🚪 Type 'exit' anytime to leave the assistant.\n")

# Chat loop
while True:
    user_input = input("🧑‍🎓 You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Until next time — stay curious and keep learning! 🧠📚")
        break

    prompt = f"{instructions}\n\nUser: {user_input}\nAssistant:"

    try:
        # generate_content returns a response object
        response = model.generate_content(prompt)
        print(f"🤖 Assistant: {response.text.strip()}\n")
    except Exception as e:
        print("⚠️ Oops! Something went wrong:", e)