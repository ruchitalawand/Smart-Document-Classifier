🧩 Overview
A Smart Document Classifier powered by transformer-based NLP models like DistilBERT. It automatically classifies text-based documents such as invoices, manuals, and reports into relevant categories based on their content. The classifier is wrapped in a FastAPI web service and ready to deploy using Docker.

🎯 Use Case
This project is designed to help organizations (like Tata Motors, banks, legal firms, etc.) automatically organize and label scanned or textual documents, streamlining workflow and reducing manual sorting.

🚀 Key Features
✅ Fine-tuned DistilBERT transformer for text classification
✅ FastAPI backend for easy integration
✅ File upload endpoint for document text prediction
✅ Lightweight and Docker-ready
✅ Easily extendable for more document types

🧠 Technologies Used
Component	Tech Used
NLP Model	HuggingFace Transformers
Web Framework	FastAPI
Language	Python 3.8+
Preprocessing	Scikit-learn, Pandas
Deployment	Docker
Inference	Uvicorn

🛠️ How It Works
Text Extraction: Accepts text documents via file upload.
Prediction: Uses a fine-tuned BERT model to predict the document category.
Response: Returns label and confidence score in JSON format.
