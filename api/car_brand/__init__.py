from fastapi import APIRouter

from api.car_brand.v1.car_brand import car_brand_router as car_brand_v1_router

router = APIRouter()
router.include_router(car_brand_v1_router, prefix="/api/v1/car-brand", tags=["Car Brand"])

__all__ = ["router"]
