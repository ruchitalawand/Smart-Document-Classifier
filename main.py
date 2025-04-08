from fastapi import FastAPI, UploadFile, File
from transformers import pipeline
import os

app = FastAPI()
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    result = classifier(text)
    return {"label": result[0]['label'], "score": float(result[0]['score'])}
