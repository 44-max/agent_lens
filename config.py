import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PRIMARY_LOCAL_MODEL = "llama3.2"  # Your specified model
OLLAMA_BASE_URL = "http://localhost:11434" # [cite: 43]