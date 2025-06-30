from fastapi import UploadFile
from services import image_service
from typing import List


async def upload_product_images(product_id: str, images: List[UploadFile]):
    return await image_service.upload_images_to_cloudinary(product_id, images)

async def fake_delete_product_image(product_id: str):
    return await image_service.fake_delete_product_image(product_id)

async def delete_product_image(product_id: str):
    return await image_service.delete_product_image(product_id)

async def get_product_images(product_id: str):
    return await image_service.get_product_images(product_id)