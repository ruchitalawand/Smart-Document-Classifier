# 📄 Smart Document Classifier

This project classifies uploaded documents (PDF, TXT, etc.) into categories like "invoice", "manual", and "specification" using a fine-tuned DistilBERT model.

## 🚀 Features
- Fine-tuned Transformer (DistilBERT) for document classification
- FastAPI-based backend for inference
- Dockerized for deployment
- Sample training notebook included

## 🧠 Tech Stack
- Python, Hugging Face Transformers
- FastAPI, Uvicorn
- Docker, scikit-learn
- Jupyter Notebook for training

## 📦 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🐳 Run with Docker

```bash
docker build -t doc-classifier .
docker run -p 8000:8000 doc-classifier
```

## 📂 API Endpoint
- `POST /predict` – Takes raw text input and returns the predicted category.
