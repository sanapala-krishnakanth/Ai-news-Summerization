from backend.config import NEWS_API_KEY

if NEWS_API_KEY:
    print("NewsAPI configuration loaded successfully!")
else:
    print("NewsAPI configuration failed.")