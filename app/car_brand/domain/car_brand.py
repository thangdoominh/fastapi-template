from sqlalchemy import Column, Unicode, BigInteger, Boolean, String, Integer
from sqlalchemy.orm import relationship

from core.database import Base
from core.database.bases import Timestamp


class CarBrand(Base, Timestamp):
    __tablename__ = "car_brands"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), nullable=False, unique=True, index=True)
    logo = Column(String)
    description = Column(String)

    # car_models = relationship("CarModel", back_populates="car_brand", nullable=True)
