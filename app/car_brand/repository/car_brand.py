from abc import ABCMeta, abstractmethod
from typing import Optional, List

from sqlalchemy import or_, select

from app.car_brand.domain import CarBrand
from core.database import session


class CarBrandRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_id(self, car_brand_id: int) -> Optional[CarBrand]:
        pass

    @abstractmethod
    async def get_by_name(
            self,
            name: str,
    ) -> Optional[CarBrand]:
        pass

    @abstractmethod
    async def get_car_brands(self) -> List[CarBrand]:
        pass

    @abstractmethod
    async def save(self, car_brand: CarBrand) -> CarBrand:
        pass

    @abstractmethod
    async def delete(self, car_brand: CarBrand) -> None:
        pass


class CarBrandSQLRepo(CarBrandRepo):

    async def get_by_id(self, car_brand_id: int) -> Optional[CarBrand]:
        return await session.get(CarBrand, car_brand_id)

    async def get_by_name(
            self,
            name: str,
    ) -> Optional[CarBrand]:
        query = await session.execute(
            select(CarBrand).where(CarBrand.name == name)
        )
        return query.scalars().first()

    async def get_car_brands(self) -> List[CarBrand]:
        query = await session.execute(select(CarBrand))
        return query.scalars().all()

    async def save(self, car_brand: CarBrand) -> CarBrand:
        session.add(car_brand)
        return car_brand

    async def delete(self, car_brand: CarBrand) -> None:
        await session.delete(car_brand)
