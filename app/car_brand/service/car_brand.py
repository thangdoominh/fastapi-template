from typing import Optional, List

from sqlalchemy import select

from app.car_brand.exception.car_brand import DuplicateCarBrandException
from core.database import session
from app.car_brand.domain import CarBrand


class CarBrandService:
    def __init__(self):
        ...

    async def get_car_list(self) -> List[CarBrand]:
        query = select(CarBrand)

        result = await session.execute(query)
        return result.scalars().all()

    async def get_car_brand(self, car_brand_id: int) -> Optional[CarBrand]:
        ...

    async def create_car_brand(self, name: str, logo: str, description: str) -> None:
        query = select(CarBrand).where(CarBrand.name == name)
        print(">>> query: ", query)
        result = await session.execute(query)
        is_exist = result.scalars().first()
        if is_exist:
            raise DuplicateCarBrandException

        brand = CarBrand(name=name, logo=logo, description=description)
        session.add(brand)
