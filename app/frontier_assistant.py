from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("OPENAI_API_KEY")

# Create client
client = OpenAI(api_key=api_key)

chat_history = []

def generate_response(user_input):

    global chat_history

    chat_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=chat_history[-10:]
    )

    reply = response.choices[0].message.content

    chat_history.append({
        "role": "assistant",
        "content": reply
    })

    return reply