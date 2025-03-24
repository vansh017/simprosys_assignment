import json
from enum import Enum
from typing import Union

from pydantic import BaseModel, Field, EmailStr


class CreateCategory(BaseModel):
    name: str
