import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing. Check your .env file.")


# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY
)


def ask_gemini(prompt: str) -> str:
    """
    Send a prompt to Gemini and return clean text.
    """

    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    response = llm.invoke(prompt)

    content = response.content

    # Handle Gemini's text-block response format
    if isinstance(content, list):
        text_parts = [
            block["text"]
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        ]

        return "\n".join(text_parts)

    return str(content)