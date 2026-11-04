from backend.news_service import search_news

query = input("Enter a topic to search for news: ").strip()

try:
    articles = search_news(query, page_size=5)

    print(f"\nFound {len(articles)} articles for: {query}")

    for index, article in enumerate(articles, start=1):
        print(f"\n{'=' * 50}")
        print(f"Article {index}")
        print("Title:", article.get("title"))
        print("Description:", article.get("description"))
        print("Source:", article.get("source", {}).get("name"))
        print("Published:", article.get("publishedAt"))
        print("URL:", article.get("url"))

except Exception as error:
    print("\nError:", error)