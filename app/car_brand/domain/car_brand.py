from sqlalchemy import Column, Unicode, BigInteger, Boolean, String

from core.database import Base
from core.database.bases import Timestamp


class CarBrand(Base, Timestamp):
    __tablename__ = "car_brand"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    logo = Column(String)
    description = Column(String)
