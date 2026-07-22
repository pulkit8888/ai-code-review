from fastapi import FastAPI

app = FastAPI(
    title="AI Code Review API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "AI Code Review Service Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }