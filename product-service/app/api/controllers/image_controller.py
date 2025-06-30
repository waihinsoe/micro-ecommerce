from db.crud import *
from bson import ObjectId
from datetime import datetime
from fastapi import UploadFile
from services import image_service

from typing import List


async def upload_product_images(product_id: str, images: List[UploadFile]):
    result = await image_service.upload_images_to_cloudinary(product_id, images)

    return result

async def fake_delete_product_image(product_id: str):
    result = await image_service.fake_delete_product_image(product_id)
    return result

async def delete_product_image(product_id: str, public_id: str):
    return