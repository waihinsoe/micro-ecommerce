from schemas.product_schema import ProductCreate, ProductInDB, ProductUpdate
from db.crud import *
from bson import ObjectId
from datetime import datetime

collection = "product_collection"

async def get_all_products():
    product_list: list = await get_all(collection)
    for product in product_list:
        if product['delete_flag'] == True:
            product_list.remove(product)
    return product_list

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




