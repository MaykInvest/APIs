#type ignore
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv() 

# Correct way to set API key
API_KEY = os.getenv("API_KEYG") 

genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')  # Use correct model name if needed

# Start chat
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat.send_message(user_input)
        print()
        print("Gemini:", response.text)
    except Exception as e:
        print("An error occurred:", e)
