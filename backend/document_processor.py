from langchain_core.documents import Document


def create_documents(articles: list) -> list:
    """
    Convert NewsAPI articles into LangChain Document objects.
    """

    documents = []

    for article in articles:
        title = article.get("title") or "Untitled"
        description = article.get("description") or ""
        content = article.get("content") or ""

        # Combine available article text
        article_text = f"""
        Title: {title}

        Description: {description}

        Content: {content}
        """

        # Store article information as metadata
        metadata = {
            "title": title,
            "source": (
                article.get("source", {}).get("name")
                if isinstance(article.get("source"), dict)
                else "Unknown"
            ),
            "url": article.get("url") or "",
            "published_at": article.get("publishedAt") or ""
        }

        document = Document(
            page_content=article_text.strip(),
            metadata=metadata
        )

        documents.append(document)

    return documents