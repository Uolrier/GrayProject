from fastapi import FastAPI


app = FastAPI(
    title="GrayProject API",
    description="""
    GrayProject Personal AI Operating System Backend.

    Provides APIs for:
    - System management
    - AI Agent services
    - Knowledge management
    - Local model interaction
    """,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.get(
    "/",
    tags=["System"],
    summary="Root endpoint",
    description="Check whether GrayProject backend is running."
)
def index():
    return {
        "project": "GrayProject",
        "status": "backend running"
    }


@app.get(
    "/health",
    tags=["System"],
    summary="Health check",
    description="Used for service monitoring."
)
def health():
    return {
        "status": "ok"
    }