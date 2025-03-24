import random

from celery import Celery
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, and_, delete
from sqlalchemy.orm import Session

from db.config import get_db
from models import UserModel
from models.categories import Categories
from models.product import Product
from schemas.product import ProductBase

CELERY_BROKER_URL = 'redis://localhost:9846/0'
CELERY_BROKER_BACKEND = 'redis://localhost:9846/0'
celery = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_BROKER_BACKEND)


product_router = APIRouter(prefix="/product")


@product_router.get("")
def api_getproducts(db: Session = Depends(get_db)):
    try:
        query = select(Product).join(Categories, and_(Product.category_id == Categories.id))
        product_list = db.execute(query).scalars().all()

        return {"product_list": product_list}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@product_router.get("/generate-products")
def api_generateproducts(db: Session = Depends(get_db)):
    try:
        generate_dummy_products(15,db=db)

        return {"product_list": []}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@product_router.post("")
def api_ceate_categories(product: ProductBase,db: Session = Depends(get_db)):
    try:

        new_product = Product(**product.model_dump())
        db.add(new_product)
        db.flush([new_product])
        db.commit()
        db.refresh(new_product)

        return {"product": new_product}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@product_router.put("/{product_id}")
def update_product(product_id : int, updated_data : ProductBase, db: Session = Depends(get_db)):
    try:
        query = select(Product).filter(Product.id == product_id)
        product = db.execute(query).scalars().all()
        if not len(product):
            raise HTTPException(status_code=404, detail="Product not found")
        product = product[0]
        for key, value in updated_data.model_dump().items():
            setattr(product, key, value)
        db.commit()
        return product

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@product_router.delete("/{product_id}")
def delete_product(product_id : int, db: Session = Depends(get_db)):
    try:
        query = delete(Product).filter(Product.id == product_id)
        db.execute(query)
        db.commit()
        return {"message": "product deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


dummy_titles = ["laptop", "Phone", "Tablet", "Headphones", "SmartWatch"]
dummy_desc = ["High quality", "Affordable", "latest", "asodhf", "Best Performance"]
dummy_prices = [754,845,78451,78,845]


@celery.task
def generate_dummy_products(num_products: int,db: Session = Depends(get_db)):
    try:
        query = select(Categories)

        all_categories = db.execute(query).scalars().all()
        category = all_categories[0]
        for _ in range(num_products):
            product = Product(
                category_id=category.id,
                title=random.choice(dummy_titles),
                description=random.choice(dummy_desc),
                price=random.choice(dummy_prices),
                status=True
            )
            db.add(product)
        db.commit()
        db.close()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
