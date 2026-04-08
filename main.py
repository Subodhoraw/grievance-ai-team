from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from transformers import pipeline
import re

# Load trained models
tfidf = joblib.load('model/tfidf_vectorizer.pkl')
dept_model = joblib.load('model/department_model.pkl')

# Load BERT sentiment model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Initialize FastAPI
app = FastAPI(title="AI Grievance System API")

# Request schema
class ComplaintRequest(BaseModel):
    text: str

# Text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# Prediction pipeline
def predict_pipeline(text):
    cleaned = clean_text(text)

    # Department prediction
    vec = tfidf.transform([cleaned])
    dept = dept_model.predict(vec)[0]

    # Sentiment prediction
    sentiment_raw = sentiment_pipeline(text[:512])[0]['label']
    sentiment = "Positive" if sentiment_raw == "POSITIVE" else "Negative"

    # Priority logic
    priority = 3 if sentiment == "Negative" else 1

    # Confidence score
    confidence = dept_model.predict_proba(vec).max()

    return {
        "complaint": text,
        "department": dept,
        "sentiment": sentiment,
        "priority": priority,
        "confidence": round(float(confidence), 2)
    }

# Root endpoint
@app.get("/")
def home():
    return {"message": "AI Grievance System Running 🚀"}

# Prediction endpoint
@app.post("/predict")
def predict(request: ComplaintRequest):
    return predict_pipeline(request.text)