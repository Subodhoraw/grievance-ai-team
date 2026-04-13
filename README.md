# 🏛️ AI-Powered Grievance Classification System

> Infotact DS/ML Internship — Project 1

Automatically classifies public grievances by **department** and **sentiment**,
then assigns a **priority score** using NLP + BERT.

## 👥 Team

| Name | Role |
|------|------|
| Subodh | Team Lead / NLP |
| Janu | Data Engineer / API |
| Kunal | ML Engineer |
| KIRAN | 

## 🚀 Quick Setup

```bash
git clone https://github.com/YOUR_USERNAME/grievance-ai-team.git
cd grievance-ai-team
pip install -r requirements.txt
```

## 📁 Project Structure

```
grievance-ai-team/
├── data/
│   ├── raw/          # Original dataset (gitignored)
│   ├── processed/    # Cleaned data (gitignored)
│   └── sample/       # 50-row sample (committed)
├── src/              # All Python modules
├── notebooks/        # Jupyter notebooks
├── models/           # Saved models (gitignored)
├── outputs/          # Charts and results
├── tests/            # Test files
└── docs/             # Documentation
```

## 📊 Results

| Model | Accuracy | Macro F1 |
|-------|----------|----------|
| Dept Classifier (SVM) | 64% | Logistic Regression |
| Sentiment (BERT) | High | Pretrained model |

## 📝 License

MIT

# 🤖 AI-Driven Citizen Grievance & Sentiment Analysis System

## 📌 Project Overview

This project focuses on building an AI-powered system to automatically process and analyze citizen grievances.

The system is designed to:

* Classify complaints into relevant government departments
* Analyze textual data efficiently
* Reduce manual effort in grievance handling

This solution aims to improve response time, transparency, and efficiency in public service systems.

---
📅* Week 1: Data Cleaning & EDA
🔧* Work Done

Loaded raw JSON dataset
Selected relevant columns:
subject_content_text → complaint
org_code → department

* Cleaned text:
- Lowercasing
- Removing special characters
- Removing missing values

📊* EDA
- WordCloud visualization
- N-gram analysis
- Complaint distribution across departments

📁* Output
data/processed/cleaned_data.csv
📅* Week 2: Department Classification
🔧 Feature Engineering
-TF-IDF Vectorization

🤖* Model
Logistic Regression
class_weight='balanced'

⚖️ * Handling Class Imbalance
Removed departments with very low samples

📊 * Evaluation
- Accuracy: ~64%
* Metrics:
- Precision
- Recall
- F1-score
- Confusion Matrix
  
📅 * Week 3: Sentiment Analysis & Priority

🤖* Model Used
Pretrained BERT (DistilBERT)

🔍* Process
Classified sentiment:
POSITIVE
NEGATIVE

⚡* Priority Logic
Sentiment	Priority
Negative	High (3)
Neutral	Medium (2)
Positive	Low (1)

✅* Outcome

* Each complaint now includes:
- Department
- Sentiment
- Priority Score
  
📅* Week 4: API & Deployment 🚀
🌐* FastAPI Backend
▶️ Run API
python -m uvicorn main:app --reload

📍 * Endpoint
POST /predict

📥*  Input
{
  "text": "Water supply is not coming for 3 days"
}
📤 Output
{
  "department": "Water",
  "sentiment": "NEGATIVE",
  "priority": 3
}

🎨* Streamlit Frontend

▶️* Run App
streamlit run streamlit_app.py

💡* Features
- Simple and clean UI
- Real-time prediction
- Displays:
- Department
- Sentiment
- Priority
  
  🧠* Key Learnings
- Importance of text preprocessing
- TF-IDF for baseline NLP models
- Power of pretrained transformers (BERT)
- Real-world deployment challenges
- 
⚠️ * Challenges Faced
- Noisy real-world data
- Class imbalance
- Dependency & environment issues
- API integration
  
🚀* Future Improvements
- Multi-language support
- Advanced transformer models (RoBERTa)
- Database integration
- Analytics dashboard for policymakers
  
* This project demonstrates how AI can:

✔ Automate grievance handling
✔ Identify urgent issues quickly
✔ Reduce manual workload
✔ Improve public service efficiency

---
