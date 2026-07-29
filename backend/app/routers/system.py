from fastapi import APIRouter

router = APIRouter(prefix="/api/system", tags=["System"])


@router.get("/health")
def health_check():
    return {"status": "ok", "service": "GrayProject Backend"}


@router.get("/info")
def system_info():
    return {"project": "GrayProject", "version": "0.1.0"}
