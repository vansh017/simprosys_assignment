from sqlalchemy import Table, Boolean, Column, Integer, String, DateTime, func
from sqlalchemy.dialects.mysql import LONGTEXT

from db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(LONGTEXT, nullable= False)
    price = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())