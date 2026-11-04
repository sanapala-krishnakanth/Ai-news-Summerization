from fastapi import APIRouter, HTTPException, Query

from backend.news_service import search_news
from backend.semantic_search import calculate_similarity
from backend.summarizer import summarize_article

router = APIRouter()


@router.get("/news/search")
def search_news_endpoint(
    query: str = Query(..., min_length=2),
    page_size: int = Query(10, ge=1, le=20)
):
    try:
        # Step 1: Fetch news articles
        articles = search_news(query, page_size)

        # Step 2: Rank articles using semantic similarity
        ranked_articles = calculate_similarity(query, articles)

        # Step 3: Generate summaries
        for article in ranked_articles:
            title = article.get("title") or ""
            description = article.get("description") or ""
            content = article.get("content") or ""

            article_text = f"{title}. {description}. {content}"

            article["summary"] = summarize_article(article_text) 

        # Step 4: Return response
        return {
            "status": "success",
            "query": query,
            "total_articles": len(ranked_articles),
            "ranking_method": "semantic_similarity",
            "summarization_model": "DistilBART",
            "articles": ranked_articles
        }

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except RuntimeError as error:
        raise HTTPException(status_code=502, detail=str(error))