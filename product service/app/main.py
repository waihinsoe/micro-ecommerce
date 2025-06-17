from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
# from app.api.routers.product_router import router as product_router
from api.routers.product_router import router as product_router # type: ignore
# from app.api.routers.image_router import router as image_router
# from app.api.routers.category_router import router as category_router

app = FastAPI(title="Product Service API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(product_router, prefix="/products", tags=["products"])
# app.include_router(image_router, prefix="/images", tags=["images"])
# app.include_router(category_router, prefix="/categories", tags=["category"])


