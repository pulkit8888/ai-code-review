from fastapi import FastAPI

from app.github.webhook import router as github_router


app = FastAPI(
    title="PRism AI",
    version="1.0.0",
    description="AI-powered GitHub Pull Request Review Platform"
)


app.include_router(
    github_router,
    prefix="/github",
    tags=["GitHub"]
)


@app.get("/")
def root():
    return {
        "message": "AI running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }