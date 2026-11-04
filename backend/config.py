
import os
from dotenv import load_dotenv

# Load environment variables from the project root .env file
load_dotenv()

# Read the NewsAPI key
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY is missing. Check your .env file.")
