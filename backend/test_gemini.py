from backend.gemini_service import ask_gemini


prompt = """
You are an AI news analyst.

Explain what ISRO does in exactly 3 bullet points

Give your answer in 5 bullet points.
"""


response = ask_gemini(prompt)

print("\nGemini Response:\n")
print(response)