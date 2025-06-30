import cloudinary # type:ignore
import cloudinary.uploader #type:ignore
from fastapi import UploadFile # type:ignore
from schemas.image_schema import ProductImageCreate, ProductImageInDB
from db.crud import *
from core.config import settings
from typing import List

from utils.image_tools import resize_and_compress_image

collection = "product_image_collection"

cloudinary.config(
    cloud_name = settings.CLOUDINARY_CLOUD_NAME,
    api_key = settings.CLOUDINARY_API_KEY,
    api_secret = settings.CLOUDINARY_API_SECRET,
    secure = True
)

async def upload_images_to_cloudinary(product_id: str, images: List[UploadFile]):
    uploaded_images = []
    try:
        count = 1
        for image in images:
            original_bytes = await image.read()
            resized_image = resize_and_compress_image(original_bytes, 1080, 85)

            upload_result = cloudinary.uploader.upload(
                resized_image,
                folder=f"products/{product_id}/images",
                format="jpg",
            )

            print(f"Upload result: {upload_result}")

            create_data = ProductImageCreate(
                product_id=product_id,
                image_url=upload_result['secure_url'],
                public_id=upload_result['public_id'],
                position=count,
                format=upload_result['format'],
            )
            print(f"\nCreate data: {create_data}")
            
            created_image = await create(collection, create_data.dict())

            uploaded_images.append({
                "id": str(created_image.inserted_id),
                "product_id": product_id,
                "image_url": upload_result['secure_url'],
                "position": count,
                "format": upload_result['format']
            })
            count += 1

            # Return the upload result
            # return {
            #     "image_url": upload_result['secure_url'],
            #     "public_id": upload_result['public_id'],
            #     "format": upload_result['format']
            # }
        print(f"Uploaded images: {uploaded_images}")
        return uploaded_images
    except Exception as e:
        raise Exception(f"Failed to upload image: {str(e)}") from e
    
async def fake_delete_product_image(product_id: str):
    try:
        images = await find(collection, product_id)        
        if not images:
            raise Exception("No images found for this product")

        for image in images:
            await patch_one(collection, image['_id'], {"delete_flag": True})
        return {"message": "Images marked as deleted successfully"}
    except Exception as e:
        raise Exception(f"Failed to mark images as deleted: {str(e)}") from e

async def delete_product_image(product_id: str):
    try:
        images = await find(collection, product_id)
        if not images:
            raise Exception("No images found for this product")

        # Delete each image from Cloudinary and the database
        for image in images:
            cloudinary.uploader.destroy(image['public_id'])
            await delete_one(collection, image['_id'])
        return {"message": "Images deleted successfully by admin"}
    except Exception as e:
        raise Exception(f"Failed to delete images: {str(e)}") from e
    
async def get_product_images(product_id: str):
    try:
        images = await find(collection, product_id)
        if not images:
            raise Exception("No images found for this product")
        
        # Convert ObjectId to string for JSON serialization
        for image in images:
            image['_id'] = str(image['_id'])
        
        print(f"Retrieved images: {images}")
        return images
    except Exception as e:
        raise Exception(f"Failed to retrieve images: {str(e)}") from e