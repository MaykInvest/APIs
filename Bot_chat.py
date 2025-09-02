"""
This script initializes a chat session with Google's Gemini language model using the `google.generativeai` library.

Functionality:
- Loads environment variables (including the Gemini API key) from a `.env` file.
- Configures the Gemini API using the API key stored in the environment variable `API_KEYG`.
- Initializes a generative chat model (Gemini 2.0 Flash variant).
- Starts an interactive terminal chat where the user can send prompts to the model and receive responses.
- The loop continues until the user types 'exit'.

Requirements:
- Environment variable `API_KEYG` must be set in a `.env` file as follows:
    API_KEYG=your_api_key_here
- `google-generativeai` and `python-dotenv` packages must be installed.

Example usage:
    You: Hello
    Gemini: Hi there! How can I assist you today?

    You: exit
    [program ends]

Note:
- The line `#type ignore` is used to suppress type-checking errors that may occur in some editors or linters.

Error Handling:
- Catches and displays any exceptions that occur during chat execution.
"""

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
