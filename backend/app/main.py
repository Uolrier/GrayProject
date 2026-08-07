import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.app.ai.rag.watcher.bootstrap import (
    init_watchers,
)
from backend.app.core.exceptions import GrayException
from backend.app.core.logger import logger
from backend.app.core.rate_limit import RateLimiter
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

limiter = RateLimiter(
    capacity=60,
    refill_rate=1,
)

watcher_manager = init_watchers()


@app.on_event("startup")
async def startup_event():
    watcher_manager.start_all()


@app.on_event("shutdown")
async def shutdown_event():
    watcher_manager.stop_all()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def rate_limit_middleware(
    request: Request,
    call_next,
):
    if os.getenv("TESTING") != "true":
        limiter.check()

    return await call_next(request)


# 注册路由
app.include_router(system.router)
app.include_router(chat.router)


@app.get("/")
def index():
    return {"project": "GrayProject", "status": "backend running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.exception_handler(GrayException)
async def gray_exception_handler(
    request: Request,
    exc: GrayException,
):
    logger.error(f"Gray Error: {exc.code} - {exc.message}")

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.code,
                "message": exc.message,
            },
        },
    )


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(f"Unhandled Exception: {request.url}")

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Internal server error",
            },
        },
    )
