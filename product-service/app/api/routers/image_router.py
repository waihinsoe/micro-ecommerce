from fastapi import APIRouter, File, UploadFile, HTTPException #type:ignore
from ..controllers import image_controller

from typing import List

router = APIRouter()

@router.post("/{product_id}/images/", status_code=201)
async def upload_image(product_id: str, images: List[UploadFile]):
    try:
        if(len(images) > 6):
            raise HTTPException(status_code=400, detail="Position must be between 1 to 6")
        else:
            return await image_controller.upload_product_images(product_id, images)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{product_id}/images/", response_model=list[dict])
async def get_images(product_id: str):
    try:
        return await image_controller.get_product_images(product_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Fake Delete For Saler
@router.put("/{product_id}/images/", status_code=200)
async def fake_delete_image(product_id: str):
    try:
        return await image_controller.fake_delete_product_image(product_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# For admin user
@router.delete("/{product_id}/images/", status_code=204)
async def delete_image(product_id: str):
    try:
        return await image_controller.delete_product_image(product_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))