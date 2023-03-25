from fastapi import APIRouter, Response, Depends


health_check_router = APIRouter()


@health_check_router.get("/health-check")
async def health_check():
    return Response(status_code=200)
