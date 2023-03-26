from typing import List, Optional

from sqlalchemy import select

from app.car_model.domain import CarModel
from app.car_model.exception.car_model import CarModelNotFoundException, DuplicateCarModelException
from core.database import session, Transactional


class CarModelService:
    def __init__(self):
        ...

    async def get_car_model_list(self) -> List[CarModel]:
        query = select(CarModel)

        result = await session.execute(query)
        models: List[CarModel] = result.scalars().all()
        return models

    async def get_car_model(self, car_model_id: int) -> Optional[CarModel]:
        query = select(CarModel).where(CarModel.id == car_model_id)
        result = await session.execute(query)
        model: CarModel = result.scalars().first()
        if not model:
            raise CarModelNotFoundException
        return model

    @Transactional()
    async def create_car_model(self, name: str, year: int, price: int, description: str, car_brand_id: int) -> None:
        query = select(CarModel).where(CarModel.name == name)
        result = await session.execute(query)
        is_exist = result.scalars().first()
        if is_exist:
            raise DuplicateCarModelException

        model = CarModel(name=name, year=year, price=price, description=description, car_brand_id=car_brand_id)
        session.add(model)

    @Transactional()
    async def update_car_model(self, car_model_id: int, name: str, year: int, price: int, description: str,
                               car_brand_id: int) -> None:
        query = select(CarModel).where(CarModel.id == car_model_id)
        result = await session.execute(query)
        model: CarModel = result.scalars().first()
        if not model:
            raise CarModelNotFoundException

        model.name = name
        model.year = year
        model.price = price
        model.description = description
        model.car_brand_id = car_brand_id

    @Transactional()
    async def delete_car_model(self, car_model_id: int) -> None:
        query = select(CarModel).where(CarModel.id == car_model_id)
        result = await session.execute(query)
        model: CarModel = result.scalars().first()
        if not model:
            raise CarModelNotFoundException

        await session.delete(model)
