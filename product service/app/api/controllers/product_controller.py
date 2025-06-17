from schemas.product_schema import ProductBase, ProductCreate, ProductInDB, ProductUpdate
from db.crud import *
from datetime import datetime

collection = "product"

async def get_all_products():
    return

async def create_product(data: ProductCreate):
    product = data.dict()
    result = await create(collection, product)
    return product

async def get_product(id: str):
    return

async def put_product(id: str, data: ProductUpdate):
    return

async def patch_product(id: str, data: ProductUpdate):
    return

async def delete_product(id: str):
    return




