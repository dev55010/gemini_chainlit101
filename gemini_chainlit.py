import chainlit as cl
from google import genai

# Initialize the Gemini client

from dotenv import load_dotenv
import os

# Configure the Gemini API
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)

@cl.on_message
async def handle_message(message):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=[{"parts": [{"data": message}]}]
    )
    await cl.Message(content=response.text).send()

if __name__ == "__main__":
    cl.run()