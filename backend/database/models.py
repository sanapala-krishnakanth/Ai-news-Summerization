from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey,
    UniqueConstraint
)

from sqlalchemy.orm import relationship

from backend.database.connection import Base


# 1. Users table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    saved_articles = relationship("SavedArticle", back_populates="user")


# 2. Articles table
class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    description = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    url = Column(String(1000), unique=True, nullable=False)
    image_url = Column(String(1000), nullable=True)
    source = Column(String(255), nullable=True)
    published_at = Column(String(100), nullable=True)
    relevance_score = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    saved_by = relationship("SavedArticle", back_populates="article")


# 3. Saved articles table
class SavedArticle(Base):
    __tablename__ = "saved_articles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    saved_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="saved_articles")
    article = relationship("Article", back_populates="saved_by")

    __table_args__ = (
        UniqueConstraint("user_id", "article_id", name="unique_saved_article"),
    )


# 4. Search history table
class SearchHistory(Base):
    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    query = Column(String(255), nullable=False)
    searched_at = Column(DateTime, default=datetime.utcnow)