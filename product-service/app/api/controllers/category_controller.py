from schemas.category_schema import CategoryBase, CategoryCreate, CategoryInDB, CategoryUpdate
from services import category_service


async def get_all_categories():
    return await category_service.get_all_categories()

async def create_category(data: CategoryCreate):
    return await category_service.create_category(data)

async def get_category(id: str):
    return await get_category(id)

async def put_category(id: str, data: CategoryUpdate):
    return await category_service.put_category(id, data)

async def patch_category(id: str, data: CategoryUpdate):
    return await category_service.patch_category(id, data) 

async def delete_category(id: str):
    return await category_service.delete_category(id)




