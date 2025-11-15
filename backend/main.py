from fastapi import FastAPI, UploadFile, File
from controllers.summarize import summarize_text
from controllers.sentiment import detect_sentiment
from controllers.ocr import extract_text_from_image

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/summarize")
def summarize_api(data: dict):
    text = data["text"]
    summary = summarize_text(text)
    return {"summary": summary}

@app.post("/sentiment")
def sentiment_api(data: dict):
    text = data["text"]
    result = detect_sentiment(text)
    return result

@app.post("/ocr")
async def ocr_api(file: UploadFile = File(...)):
    text = extract_text_from_image(file)
    return {"extracted_text": text}
