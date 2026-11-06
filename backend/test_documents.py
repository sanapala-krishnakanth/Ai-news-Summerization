from backend.news_service import search_news
from backend.document_processor import create_documents


# Fetch 3 news articles
articles = search_news("artificial intelligence", page_size=3)

# Convert articles into LangChain Documents
documents = create_documents(articles)

print("Total documents created:", len(documents))

for index, document in enumerate(documents, start=1):
    print(f"\nDocument {index}")
    print("Title:", document.metadata["title"])
    print("Source:", document.metadata["source"])
    print("URL:", document.metadata["url"])
    print("Content:", document.page_content[:300])