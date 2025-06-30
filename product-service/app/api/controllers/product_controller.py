from services import product_service
from schemas.product_schema import ProductCreate, ProductInDB, ProductUpdate

async def get_all_products():
    return await product_service.get_all_products()

async def create_product(data: ProductCreate):
    return await product_service.create_product(data)

async def get_product(id: str):
    return await get_product(id)

async def put_product(id: str, data: ProductUpdate):
    return await product_service.put_product(id, data)

async def patch_product(id: str, data: ProductUpdate):
    return await product_service.patch_product(id, data)

async def delete_product(id: str):  
    return await delete_product(id)




