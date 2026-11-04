from fastapi import FastAPI
from backend.routes import router

app = FastAPI(
    title="AI News Summarizer API",
    description="Backend API for the AI-powered News Summarizer application",
    version="1.0.0"
)


app.include_router(router, prefix="/api", tags=["News"])


@app.get("/")
def root():
    return {
        "message": "Welcome to AI News Summarizer API",
        "status": "Running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "application": "AI News Summarizer"
    }