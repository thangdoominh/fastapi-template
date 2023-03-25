# from typing import Optional
#
# from app.car_brand.exception.car_brand import CarBrandNotFoundException
# from app.car_brand.repository import CarBrandRepo
# from app.car_brand.schema import CarBrandSchema
#
#
# class CarBrandQueryService:
#     def __init__(self, car_brand_repo: CarBrandRepo):
#         self.car_brand_repo = car_brand_repo
#
#     async def get_car_brand(self, car_brand_id: int) -> Optional[CarBrandSchema]:
#         car_brand = await self.car_brand_repo.get_by_id(car_brand_id=car_brand_id)
#         if not car_brand:
#             raise CarBrandNotFoundException
#
#         return CarBrandSchema.from_orm(car_brand)
#
