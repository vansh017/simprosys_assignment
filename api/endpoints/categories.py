from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.config import get_db
from models import UserModel
from models.categories import Categories
from schemas.categories import CreateCategory

categories_router = APIRouter(prefix="/categories")


@categories_router.get("")
def api_getcategories(db: Session = Depends(get_db)):
    try:
        query = select(Categories)
        category_list = db.execute(query).scalars().all()

        return {"category_list": category_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")




@categories_router.post("")
def api_ceate_categories(category: CreateCategory,db: Session = Depends(get_db)):
    try:
        query = select(Categories).filter(Categories.name == category.name)

        category_list = db.execute(query).scalars().all()

        if category_list:
            raise HTTPException(status_code=400, detail=f"category already present")

        new_category = Categories(**category.model_dump())
        db.add(new_category)
        db.flush([new_category])
        db.commit()
        db.refresh(new_category)

        return {"category": new_category}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
