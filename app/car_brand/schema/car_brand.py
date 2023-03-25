from datetime import datetime

from pydantic import BaseModel, Field


class GetCarBrandListResponseSchema(BaseModel):
    id: int = Field(..., description="ID")
    name: str = Field(..., description="Name")
    logo: str = Field(..., description="Logo")
    description: str = Field(..., description="Description")
    created_at: datetime = Field(None, description="Create Time")
    updated_at: datetime = Field(None, description="Update Time")

    class Config:
        orm_mode = True


class CreateCarBrandRequestSchema(BaseModel):
    name: str = Field(..., description="Name")
    logo: str = Field(..., description="Logo")
    description: str = Field(..., description="Description")


class CreateCarBrandResponseSchema(BaseModel):
    id: int = Field(None, description="ID")
    name: str = Field(None, description="Name")
    logo: str = Field(None, description="Logo")
    description: str = Field(None, description="Description")
    created_at: datetime = Field(None, description="Create Time")
    updated_at: datetime = Field(None, description="Update Time")

    class Config:
        orm_mode = True
