from db.crud import *
from bson import ObjectId
from datetime import datetime
from fastapi import UploadFile
from services import image_service


async def upload_product_images(product_id: str, position: int, file: UploadFile):
    result = await image_service.upload_images_to_cloudinary(product_id, position, file)

    return {
        "product_id": product_id,
        "image_url": result['image_url'],
        "public_id": result['public_id'],
    }