from backend.semantic_search import calculate_similarity

query = "ind vs nz odi"

articles = [
    {
        "title": "India and New Zealand ODI series",
        "description": "India prepares for the upcoming cricket series."
    },
    {
        "title": "Latest artificial intelligence developments",
        "description": "New AI models and technology updates."
    },
    {
        "title": "New Zealand cricket team announces squad",
        "description": "The team prepares for its ODI matches against India."
    }
]

results = calculate_similarity(query, articles)

for article in results:
    print("\nTitle:", article["title"])
    print("Similarity:", article["relevance_score"])