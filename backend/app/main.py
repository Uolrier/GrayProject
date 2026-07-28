from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import GrayException
from app.core.logger import logger


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


@app.get("/")
def index():
    return {
        "project": "GrayProject",
        "status": "backend running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.exception_handler(GrayException)
async def gray_exception_handler(
    request: Request,
    exc: GrayException
):

    logger.error(
        f"API Error: {exc.code} - {exc.message}"
    )

    return JSONResponse(
        status_code=400,
        content={
            "code": exc.code,
            "message": exc.message
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(
        f"Unhandled Exception: {request.url}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "code": "INTERNAL_ERROR",
            "message": "Internal server error"
        }
    )