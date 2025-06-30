from schemas.category_schema import CategoryBase, CategoryCreate, CategoryInDB, CategoryUpdate
from db.crud import *
from bson import ObjectId 
from datetime import datetime

collection = "category_collection"

async def get_all_categories():
    category_list: list = await get_all(collection)
    for category in category_list:
        if category['delete_flag'] == True:
            category_list.remove(category)
    return category_list

async def create_category(data: CategoryCreate):
    category = data.dict()
    get_all_categories = await get_all(collection)
    for cat in get_all_categories:
        if cat['name'] == category['name']:
            return None
    result = await create(collection, category)
    return category

async def get_category(id: str):
    return await get_one(collection, id)

async def put_category(id: str, data: CategoryUpdate):
    await update_one(collection, id, data.dict())
    updated = await get_one(collection, id)
    print("updated:", updated)
    return updated

async def patch_category(id: str, data: CategoryUpdate):
    await patch_one(collection, id, data.dict())
    patched = await get_one(collection, id)
    return patched 

async def delete_category(id: str):
    return await delete_one(collection, ObjectId(id))


