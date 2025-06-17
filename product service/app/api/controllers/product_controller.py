from schemas.product_schema import ProductBase, ProductCreate, ProductInDB, ProductUpdate
from db.crud import *
from bson import ObjectId
from datetime import datetime

collection = "product"

async def get_all_products():
    return await get_all(collection)

async def create_product(data: ProductCreate):
    product = data.dict()
    result = await create(collection, product)
    return product

async def get_product(id: str):
    return await get_one(collection, id)

async def put_product(id: str, data: ProductUpdate):
    await update_one(collection, id, data.dict())
    updated = await get_one(collection, id)
    return updated

async def patch_product(id: str, data: ProductUpdate):
    await patch_one(collection, id, data.dict())
    patched = await get_one(collection, id)
    return patched 

async def delete_product(id: str):
    return await delete_one(collection, ObjectId(id))




