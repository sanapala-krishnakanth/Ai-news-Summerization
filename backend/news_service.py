import requests

from backend.config import NEWS_API_KEY


NEWS_API_URL = "https://newsapi.org/v2/everything"


def search_news(query: str, page_size: int = 10) -> list:
    """
    Fetch news articles from NewsAPI.org using a search keyword.
    """

    if not query or not query.strip():
        raise ValueError("Search query cannot be empty.")

    headers = {
        "X-Api-Key": NEWS_API_KEY
    }

    params = {
    "q": query,
    "searchIn": "title,description",
    "language": "en",
    "sortBy": "relevancy",
    "pageSize": page_size
}

    try:
        response = requests.get(
            NEWS_API_URL,
            headers=headers,
            params=params,
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        if data.get("status") != "ok":
            raise RuntimeError(data.get("message", "NewsAPI request failed."))

        return data.get("articles", [])

    except requests.exceptions.HTTPError as error:
        try:
            message = response.json().get("message", str(error))
        except ValueError:
            message = str(error)

        raise RuntimeError(f"NewsAPI HTTP error: {message}") from error

    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Unable to connect to NewsAPI: {error}") from error