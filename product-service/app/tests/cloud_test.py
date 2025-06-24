import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config( 
    cloud_name = "dpgxgj5ea", 
    api_key = "748184226436125", 
    api_secret = "-GuD5TvgT90g1A9UzfAxYBF8EbQ", # Click 'View API Keys' above to copy your API secret
    secure=True
)

# Upload an image
upload_result = cloudinary.uploader.upload("https://res.cloudinary.com/demo/image/upload/getting-started/shoes.jpg",
                                           public_id="shoes")
print(upload_result["secure_url"])

# Optimize delivery by resizing and applying auto-format and auto-quality
optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
print(optimize_url)

# Transform the image: auto-crop to square aspect_ratio
auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
print(auto_crop_url)


# Cloud name = dpgxgj5ea
# api key = 748184226436125
# api secret = -GuD5TvgT90g1A9UzfAxYBF8EbQ
# API environment variable = CLOUDINARY_URL=cloudinary://748184226436125:-GuD5TvgT90g1A9UzfAxYBF8EbQ@dpgxgj5ea