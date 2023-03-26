from typing import List

from fastapi import APIRouter, Response

from app.car_brand.schema import ExceptionResponseSchema
from app.car_model.schema.car_model import GetCarModelResponseSchema, CreateCarModelRequestSchema, \
    CreateCarModelResponseSchema
from app.car_model.service.car_model import CarModelService

car_model_router = APIRouter()


@car_model_router.get(
    "",
    response_model=List[GetCarModelResponseSchema],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_car_model_list():
    return await CarModelService().get_car_model_list()


@car_model_router.post(
    "",
    response_model=CreateCarModelResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create a car model"
)
async def create_car_model(request: CreateCarModelRequestSchema):
    await CarModelService().create_car_model(**request.dict())
    return Response(status_code=201)


@car_model_router.get(
    "/{car_model_id}",
    response_model=GetCarModelResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Get a car model"
)
async def get_car_model(car_model_id: int):
    return await CarModelService().get_car_model(car_model_id=car_model_id)


@car_model_router.put(
    "/{car_model_id}",
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Update a car model"
)
async def update_car_model(car_model_id: int, request: CreateCarModelRequestSchema):
    await CarModelService().update_car_model(car_model_id=car_model_id, **request.dict())
    return Response(status_code=204)


@car_model_router.delete(
    "/{car_model_id}",
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Delete a car model"
)
async def delete_car_model(car_model_id: int):
    await CarModelService().delete_car_model(car_model_id=car_model_id)
    return Response(status_code=204)
