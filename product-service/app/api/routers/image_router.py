from fastapi import APIRouter, File, UploadFile, HTTPException
from ..controllers import image_controller

router = APIRouter()

@router.post("/{product_id}/images/", status_code=201)
async def upload_image(product_id: str, position: int, file: UploadFile = File(...)):
    try:
        return await image_controller.upload_product_images(product_id, position, file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @router.get("/{product_id}/images/", response_model=list[dict])
# async def get_images(product_id: str):
#     try:
#         # Fetch images from Cloudinary
#         resources = cloudinary.api.resources(type="upload", prefix=f"products/{product_id}/images", max_results=100)
        
#         # Return a list of image URLs and public IDs
#         return [
#             {
#                 "image_url": resource['secure_url'],
#                 "public_id": resource['public_id'],
#                 "format": resource['format']
#             } for resource in resources['resources']
#         ]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# @router.delete("/{product_id}/images/{public_id}", status_code=204)
# async def delete_image(product_id: str, public_id: str):
#     try:
#         # Delete the image from Cloudinary
#         cloudinary.uploader.destroy(public_id)
#         return
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))