import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# List available models
for model in genai.list_models():
    print(f"Model name: {model.name}")
    print(f"Display name: {model.display_name}")
    print(f"Description: {model.description}")
    print(f"Generation methods: {model.supported_generation_methods}")
    print("-" * 80)
