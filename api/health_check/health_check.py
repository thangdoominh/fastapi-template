from fastapi import APIRouter, Response

health_check_router = APIRouter()


@health_check_router.get("/health-check", tags=["Health Check"])
async def health_check():
    return Response(status_code=200)
