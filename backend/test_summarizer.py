from backend.summarizer import summarize_article

article = """
Artificial intelligence is transforming many industries around
the world. Companies are using AI to automate repetitive tasks,
improve customer experiences, analyze large amounts of data,
and support better decision-making. Researchers are also
developing new language models that can understand and generate
human language. However, AI systems still face challenges
related to reliability, privacy, bias, and responsible usage.
"""

summary = summarize_article(article)

print("\nOriginal Article:\n")
print(article)

print("\nGenerated Summary:\n")
print(summary)