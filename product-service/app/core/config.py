from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    MONGO_URI: str = Field(..., env="MONGO_URI")
    MONGO_DB: str = Field(..., env="MONGO_DB")

    CLOUDINARY_CLOUD_NAME: str = Field(..., env="CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY: str = Field(..., env="CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET: str = Field(..., env="CLOUDINARY_API_SECRET")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()