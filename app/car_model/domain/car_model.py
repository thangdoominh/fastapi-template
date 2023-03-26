from core.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Unicode
from sqlalchemy.orm import relationship


class CarModel(Base):
    __tablename__ = "car_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Unicode(255), nullable=False, unique=True, index=True)
    year = Column(Integer)
    price = Column(Integer)
    description = Column(String)
    car_brand_id = Column(Integer, ForeignKey("car_brand.id"))

    car_brand = relationship("CarBrand", back_populates="car_models")
