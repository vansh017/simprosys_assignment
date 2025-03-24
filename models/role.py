# models.py
from pydantic import EmailStr
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT

from db import Base


class RoleModel(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(LONGTEXT)

