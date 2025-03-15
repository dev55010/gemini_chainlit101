from google import genai
# from dotenv import 

from dotenv import load_dotenv
import os

# Configure the Gemini API
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=gemini_api_key)


client = genai.Client(api_key=gemini_api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)
