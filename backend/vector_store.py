from langchain_community.vectorstores import FAISS

from backend.embeddings import NewsEmbeddings


# Initialize embedding model
embedding_model = NewsEmbeddings()


def create_vector_store(documents: list):
    """
    Convert documents into embeddings and store them in FAISS.
    """

    if not documents:
        raise ValueError("No documents provided to create the vector store.")

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embedding_model
    )

    return vector_store


def search_vector_store(vector_store, question: str, k: int = 3):
    """
    Retrieve the most relevant news documents for a question.
    """

    if not question or not question.strip():
        raise ValueError("Search question cannot be empty.")

    results = vector_store.similarity_search_with_score(
        question,
        k=k
    )

    return results