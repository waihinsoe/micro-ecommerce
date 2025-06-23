from fastapi import APIRouter, HTTPException #type:ignore
from schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryInDB
from ..controllers import category_controller

router = APIRouter()


@router.get("/", response_model=list[ProductInDB])
async def get_all_categories():
    return await product_controller.get_all_products()

@router.post("/", response_model=ProductCreate, status_code=201)
async def create_category(data: ProductCreate):
    return await product_controller.create_product(data)

@router.get("/{product_id}", response_model=ProductInDB)
async def get_category(product_id: str):
    product = await product_controller.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductInDB)
async def put_product(product_id: str, data: ProductUpdate):
    product = await product_controller.put_product(product_id, data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.patch("/{product_id}", response_model=ProductInDB)
async def patch_product(product_id: str, data: ProductUpdate):
    product = await product_controller.patch_product(product_id, data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product 

@router.delete("/{product_id}", status_code=204)
async def delete_product(product_id: str):
    await product_controller.delete_product(product_id)
    return

