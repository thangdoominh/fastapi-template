from datetime import datetime

from pydantic import BaseModel, Field


class GetCarModelResponseSchema(BaseModel):
    id: int = Field(..., description="ID")
    name: str = Field(..., description="Name")
    year: int = Field(..., description="Year")
    description: str = Field(..., description="Description")
    price: int = Field(..., description="Price")
    car_brand_id: int = Field(..., description="Car Brand ID")
    created_at: datetime = Field(None, description="Create Time")
    updated_at: datetime = Field(None, description="Update Time")

    class Config:
        orm_mode = True


class CreateCarModelRequestSchema(BaseModel):
    name: str = Field(..., description="Name")
    year: int = Field(..., description="Year")
    description: str = Field(..., description="Description")
    price: int = Field(..., description="Price")
    car_brand_id: int = Field(..., description="Car Brand ID")


class CreateCarModelResponseSchema(BaseModel):
    id: int = Field(None, description="ID")
    name: str = Field(None, description="Name")
    year: int = Field(None, description="Year")
    price: int = Field(None, description="Price")
    description: str = Field(..., description="Description")
    car_brand_id: int = Field(None, description="Car Brand ID")
    created_at: datetime = Field(None, description="Create Time")
    updated_at: datetime = Field(None, description="Update Time")

    class Config:
        orm_mode = True
