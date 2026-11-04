from transformers import pipeline

# Load pretrained DistilBART model
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)


def summarize_article(text: str) -> str:

    if not text or not text.strip():
        raise ValueError("Article text cannot be empty.")

    # Generate summary
    result = summarizer(
        text,
        max_length=100,
        min_length=20,
        do_sample=False,
        truncation=True
    )

    return result[0]["summary_text"]