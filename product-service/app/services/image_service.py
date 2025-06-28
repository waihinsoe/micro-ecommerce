import cloudinary
import cloudinary.uploader
from fastapi import UploadFile
from schemas.image_schema import ProductImageCreate, ProductImageInDB, ProductImageUpdate
from db.crud import *
from core.config import settings

import logging


logger = logging.getLogger(__name__)

collection = "product_image_collection"

cloudinary.config(
    cloud_name = settings.CLOUDINARY_CLOUD_NAME,
    api_key = settings.CLOUDINARY_API_KEY,
    api_secret = settings.CLOUDINARY_API_SECRET,
    secure = True
)

async def upload_images_to_cloudinary(product_id: str, position: int, file: UploadFile):
    try:
        logger.info("Image Service is ready")
        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload(
            file.file,
            folder=f"products/{product_id}/images",
            use_filename=True,
            unique_filename=False
        )

        print(f"Upload result: {upload_result}")

        create_data = ProductImageCreate(
            product_id=product_id,
            image_url=upload_result['secure_url'],
            public_id=upload_result['public_id'],
            position=position,
        )
        print(f"Create data: {create_data}")
        
        await create(collection, create_data.dict())

        # Return the upload result
        return {
            "image_url": upload_result['secure_url'],
            "public_id": upload_result['public_id'],
            "format": upload_result['format']
        }
    except Exception as e:
        raise Exception(f"Failed to upload image: {str(e)}") from e