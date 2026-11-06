from backend.news_service import search_news
from backend.document_processor import create_documents
from backend.vector_store import create_vector_store, search_vector_store


# 1. Fetch news articles
articles = search_news("artificial intelligence", page_size=5)

# 2. Convert articles into LangChain Documents
documents = create_documents(articles)

print("Documents created:", len(documents))

# 3. Create FAISS vector store
vector_store = create_vector_store(documents)

print("FAISS vector store created successfully!")

# 4. Search using a question
question = "How is artificial intelligence changing technology?"

results = search_vector_store(
    vector_store,
    question,
    k=3
)

# 5. Display retrieved articles
print("\nRetrieved Articles:\n")

for index, (document, distance) in enumerate(results, start=1):
    print(f"\nResult {index}")
    print("Title:", document.metadata["title"])
    print("Source:", document.metadata["source"])
    print("Distance:", round(float(distance), 4))
    print("URL:", document.metadata["url"]) 