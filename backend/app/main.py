from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Business Intelligence Copilot",
    description="AI-powered Business Intelligence API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI BI Copilot API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }