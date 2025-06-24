from fastapi import APIRouter, HTTPException #type:ignore
from schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryInDB
from ..controllers import category_controller

router = APIRouter()


@router.get("/", response_model=list[CategoryInDB])
async def get_all_categories():
    return await category_controller.get_all_categories()

@router.post("/", response_model=CategoryCreate, status_code=201)
async def create_category(data: CategoryCreate):
    print(data)
    result = await category_controller.create_category(data)
    if not result:
        raise HTTPException(status_code=400, detail="Category with this name already exists.")
    return result

@router.get("/{category_id}", response_model=CategoryInDB)
async def get_category(category_id: str):
    category = await category_controller.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=CategoryInDB)
async def put_category(category_id: str, data: CategoryUpdate):
    category = await category_controller.put_category(category_id, data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.patch("/{category_id}", response_model=CategoryInDB)
async def patch_category(category_id: str, data: CategoryUpdate):
    category = await category_controller.patch_category(category_id, data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category 

@router.delete("/{category_id}", status_code=204)
async def delete_category(category_id: str):
    await category_controller.delete_category(category_id)
    return

