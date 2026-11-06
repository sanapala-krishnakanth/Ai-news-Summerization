from sqlalchemy.orm import Session

from backend.database.models import Article, SearchHistory


def save_search_history(db: Session, query: str):
    """Store a user's news search query."""

    search_record = SearchHistory(
        query=query
    )

    db.add(search_record)
    db.commit()


def save_articles(db: Session, articles: list):
    """Save news articles or update existing ones using their URLs."""

    for article_data in articles:
        url = article_data.get("url")

        if not url:
            continue

        existing_article = (
            db.query(Article)
            .filter(Article.url == url)
            .first()
        )

        if existing_article:
            existing_article.summary = article_data.get("summary")
            existing_article.relevance_score = article_data.get(
                "relevance_score"
            )
        else:
            article = Article(
                title=article_data.get("title") or "Untitled",
                description=article_data.get("description"),
                summary=article_data.get("summary"),
                url=url,
                image_url=article_data.get("urlToImage"),
                source=(
                    article_data.get("source", {}).get("name")
                    if isinstance(article_data.get("source"), dict)
                    else None
                ),
                published_at=article_data.get("publishedAt"),
                relevance_score=article_data.get("relevance_score")
            )

            db.add(article)

    db.commit()