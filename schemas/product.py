import json
from enum import Enum
from typing import Union

from pydantic import BaseModel, Field, EmailStr


class ProductBase(BaseModel):
    category_id: int
    title: str
    description: str = None
    price: float
    status: bool = True
