# from app.car_brand.domain import CarBrand
# from app.car_brand.exception.car_brand import DuplicateCarBrandException
# from app.car_brand.schema import CarBrandSchema
# from sqlalchemy import select
#
# from core.database import session
#
#
# class CarBrandCommandService:
#     def __init__(self):
#         pass
#
#     def create_car_brand(self, name: str, logo: str, description: str) -> CarBrandSchema:
#         query = select(CarBrand).where(CarBrand.name == name)
#         result = await session.execute(query)
#         is_exist = result.scalars().first()
#         if is_exist:
#             raise DuplicateCarBrandException
#
#         brand = CarBrand(name=name, logo=logo, description=description)
#         session.add(brand)
