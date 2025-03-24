from sqlalchemy import Table, Boolean, Column, Integer, String, DateTime, func
from sqlalchemy.dialects.mysql import LONGTEXT

from db import Base


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key= True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(LONGTEXT, nullable=False)
    email = Column(String(50), nullable=False)


