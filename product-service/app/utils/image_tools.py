from PIL import Image
import io


def resize_and_compress_image(file_bytes: bytes, max_width: int = 1080, quality: int = 85) -> io.BytesIO:
    image = Image.open(io.BytesIO(file_bytes))

    if image.width > max_width:
        ratio = max_width / image.width
        new_height = int(image.height * ratio)
        image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)

    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")

    output_buffer = io.BytesIO()
    image.save(output_buffer, format="JPEG", quality=quality, optimize=True)
    output_buffer.seek(0)
    return output_buffer