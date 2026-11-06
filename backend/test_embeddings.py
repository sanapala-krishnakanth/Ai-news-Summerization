from backend.embeddings import NewsEmbeddings
from sentence_transformers.util import cos_sim

# Initialize embedding model
embedding_model = NewsEmbeddings()

# Different concepts
documents = [
    "Doctors use artificial intelligence to detect diseases from medical scans.",
    "Space agencies launch rockets to explore planets and study the universe.",
    "Farmers use smart irrigation systems to improve crop production.",
    "Cybersecurity experts protect computer networks from hackers and malware.",
    "Banks use machine learning to detect fraudulent financial transactions."
]

# Different questions
questions = [
    "How can technology help doctors diagnose patients?",
    "How do scientists explore outer space?",
    "How can farmers save water?",
    "How do organizations protect their computer systems?",
    "How can banks identify suspicious transactions?"
]

# Generate document embeddings
document_vectors = embedding_model.embed_documents(documents)

# Test each question
for question in questions:

    query_vector = embedding_model.embed_query(question)

    similarities = cos_sim(
        query_vector,
        embedding_model.model.encode(
            documents,
            convert_to_tensor=True,
            normalize_embeddings=True
        )
    )[0]

    print("\nQuestion:", question)

    best_index = similarities.argmax().item()

    print("Best matching concept:", documents[best_index])
    print("Similarity score:", round(similarities[best_index].item(), 4))