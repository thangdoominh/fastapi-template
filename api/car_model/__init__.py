from fastapi import APIRouter

from api.car_model.v1.car_model import car_model_router as car_model_v1_router

router = APIRouter()
router.include_router(car_model_v1_router, prefix="/api/v1/car-model", tags=["Car Model"])

__all__ = ["router"]
