from sentence_transformers import SentenceTransformer
from langchain_core.embeddings import Embeddings


class NewsEmbeddings(Embeddings):
    """
    Convert news articles and user questions into numerical vectors.
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        vectors = self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True
        )

        return vectors.tolist()

    def embed_query(self, text: str) -> list[float]:
        vector = self.model.encode(
            text,
            normalize_embeddings=True,
            convert_to_numpy=True
        )

        return vector.tolist()