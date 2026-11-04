from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# Load the pretrained semantic model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(query, articles):

    if not articles:
        return []

    # Convert the search query into an embedding
    query_embedding = model.encode(
        query,
        convert_to_tensor=True
    )

    article_texts = []

    # Combine each article's title and description
    for article in articles:
        title = article.get("title") or ""
        description = article.get("description") or ""

        article_texts.append(f"{title}. {description}")

    # Convert article text into embeddings
    article_embeddings = model.encode(
        article_texts,
        convert_to_tensor=True
    )

    # Calculate cosine similarity
    scores = cos_sim(query_embedding, article_embeddings)[0]

    results = []

    for index, article in enumerate(articles):
        article["relevance_score"] = round(
            scores[index].item(), 4
        )
        results.append(article)

    # Highest similarity first
    results.sort(
        key=lambda article: article["relevance_score"],
        reverse=True
    )

    return results