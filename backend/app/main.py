from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.app.core.exceptions import GrayException
from backend.app.core.logger import logger
from backend.app.routers import chat, system

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
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 注册路由
app.include_router(system.router)
app.include_router(chat.router)


@app.get("/")
def index():
    return {"project": "GrayProject", "status": "backend running"}


@app.exception_handler(GrayException)
async def gray_exception_handler(request: Request, exc: GrayException):
    logger.error(f"API Error: {exc.code} - {exc.message}")

    return JSONResponse(
        status_code=400, content={"code": exc.code, "message": exc.message}
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled Exception: {request.url}")

    return JSONResponse(
        status_code=500,
        content={"code": "INTERNAL_ERROR", "message": "Internal server error"},
    )
