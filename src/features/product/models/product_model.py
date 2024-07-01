from datetime import datetime
from pydantic import BaseModel


class ProductCreateModel(BaseModel):
    """Model used when creating a new product"""

    name: str
    price: int


class ProductModel(BaseModel):
    """Model used when dealing with product record from database"""

    id: int
    name: str
    price: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

    def __str__(self) -> str:
        return f"ProductModel(id={self.id}, name={self.name}, price={self.price})"  # noqa: E501
