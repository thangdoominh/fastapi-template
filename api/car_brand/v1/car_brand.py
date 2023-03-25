from fastapi import APIRouter, Depends, Response

from app.car_brand.schema import ExceptionResponseSchema
from app.car_brand.schema.car_brand import CreateCarBrandResponseSchema, CreateCarBrandRequestSchema
from app.car_brand.service import CarBrandService

car_brand_router = APIRouter()


@car_brand_router.post(
    "",
    response_model=CreateCarBrandResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create a car brand"
)
async def create_car_brand(request: CreateCarBrandRequestSchema):
    await CarBrandService().create_car_brand(**request.dict())
    return Response(status_code=201)
