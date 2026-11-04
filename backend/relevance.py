import re
from urllib.parse import urlparse


def normalize_word(word):
    """Normalize simple plural forms."""
    word = word.lower()

    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"

    if len(word) > 3 and word.endswith("s"):
        return word[:-1]

    return word


def tokenize(text):
    """Convert text into normalized words."""
    words = re.findall(r"[a-zA-Z0-9]+", text.lower())

    return {
        normalize_word(word)
        for word in words
        if len(word) > 1
    }


def rank_articles(query, articles):
    """Filter duplicates and rank articles by keyword relevance."""

    query_words = tokenize(query)

    if not query_words:
        return []

    scored_articles = []
    seen_articles = set()

    for article in articles:

        title = article.get("title") or ""
        description = article.get("description") or ""
        url = article.get("url") or ""

        # Remove duplicate articles using URL
        if url:
            unique_id = urlparse(url)._replace(
                query="", fragment=""
            ).geturl().lower()
        else:
            unique_id = title.lower().strip()

        if not unique_id or unique_id in seen_articles:
            continue

        seen_articles.add(unique_id)

        # Extract keywords
        title_words = tokenize(title)
        description_words = tokenize(description)

        # Calculate relevance score
        title_matches = len(query_words & title_words)
        description_matches = len(query_words & description_words)

        score = (title_matches * 3) + description_matches

        # Give additional weight to an exact phrase in the title
        if query.lower().strip() in title.lower():
            score += 4

        # Ignore articles with no matching keywords
        if score == 0:
            continue

        scored_articles.append((score, article))

    # Sort by relevance score, highest first
    scored_articles.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [article for score, article in scored_articles]