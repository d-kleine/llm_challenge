import openai
import os
from dotenv import load_dotenv  # Add

load_dotenv()  # Add

openai.api_key = os.getenv("OPENAI_API_KEY")
