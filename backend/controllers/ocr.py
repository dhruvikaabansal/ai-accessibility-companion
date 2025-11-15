import io

def extract_text_from_image(upload_file):
    try:
        from PIL import Image
        import pytesseract
    except Exception:
        return "OCR libraries not installed on the server. Install pillow and pytesseract to enable OCR."

    try:
        image_bytes = upload_file.file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        text = pytesseract.image_to_string(image)
        cleaned = text.strip()
        if not cleaned:
            return "No text detected in the image."
        return cleaned
    except Exception as e:
        return f"OCR failed: {e}"
