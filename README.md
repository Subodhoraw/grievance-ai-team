# 🏛️ AI-Powered Grievance Classification System

> Infotact DS/ML Internship — Project 1

Automatically classifies public grievances by **department** and **sentiment**,
then assigns a **priority score** using NLP + BERT.

## 👥 Team

| Name | Role |
|------|------|
| Subodh | Team Lead / NLP |
| KIRAN | ML Engineer |
| Janu | Data Engineer |
| Kunal | API / DevOps |

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

*(To be updated after Week 3)*

| Model | Accuracy | Macro F1 |
|-------|----------|----------|
| Dept Classifier (SVM) | — | — |
| Sentiment (BERT) | — | — |

## 🔌 API Usage

*(To be updated after Week 4)*

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

# 📅 Week 1: Data Collection, Cleaning & EDA

## 🎯 Objective

The primary goal of Week 1 was to transform raw grievance data into a structured and clean format suitable for machine learning.

---

## 📂 Dataset Description

The dataset contains citizen complaints submitted to various departments, along with metadata.

### Key Features Used:

* **Complaint Text** (`subject_content_text`) → Input feature
* **Department Code** (`org_code`) → Target variable

---

## 🧹 Data Preprocessing

The raw dataset required extensive cleaning:

* Extracted only relevant columns
* Renamed columns for clarity:

  * `subject_content_text` → `complaint`
  * `org_code` → `department`
* Removed missing and invalid entries
* Standardized text by:

  * Converting to lowercase
  * Removing special characters
  * Cleaning unnecessary formatting

---

## 📊 Exploratory Data Analysis (EDA)

To understand the data better:

* Generated **WordCloud** to visualize frequently used words
* Performed **N-gram analysis** to identify common phrase patterns
* Analyzed distribution of complaints across departments

---

## 💾 Data Storage

The cleaned dataset was saved in:

```
data/processed/cleaned_data.csv
```

This ensures reproducibility and separation of raw vs processed data.

---

## ✅ Week 1 Outcome

* Converted raw JSON data into structured format
* Cleaned and prepared dataset for modeling
* Identified key patterns using EDA

---

# 📅 Week 2: Department Classification Model

## 🎯 Objective

The goal of Week 2 was to build a machine learning model to automatically classify complaints into appropriate government departments.

---

## 🔢 Feature Engineering

Text data was transformed into numerical format using:

* **TF-IDF (Term Frequency-Inverse Document Frequency)**

This helps capture the importance of words in each complaint.

---

## ✂️ Data Splitting

The dataset was divided into:

* Training set (80%)
* Testing set (20%)

This allows evaluation on unseen data.

---

## 🤖 Model Development

A **Logistic Regression** model was implemented as the baseline classifier.

Enhancements applied:

* Increased iterations (`max_iter=300`)
* Used `class_weight='balanced'` to address imbalance

---

## ⚖️ Handling Class Imbalance

The dataset had many departments with very few samples.

To improve performance:

* Rare classes were removed
* Balanced class weights were applied

---

## 📊 Model Evaluation

The model was evaluated using:

* Accuracy Score
* Precision, Recall, F1-score
* Confusion Matrix

---

## 📈 Results

* Achieved ~64% baseline accuracy
* Improved classification performance after handling imbalance
* Better predictions for frequently occurring departments

---

## ✅ Week 2 Outcome

* Successfully built and trained classification model
* Improved model performance using practical techniques
* Automated routing of complaints to departments

---

# 🧠 Key Learnings

* Real-world data requires extensive preprocessing
* Text must be converted into numerical form for ML models
* Class imbalance significantly impacts model performance
* Evaluation metrics beyond accuracy are critical

---

# 🚀 Next Steps (Week 3)

* Perform Sentiment Analysis on complaints
* Assign priority scores based on urgency
* Build a dual-output system (Department + Sentiment)

---

# 🏁 Conclusion

By the end of Week 2, a functional AI system has been developed that can automatically classify citizen complaints into appropriate departments.

This forms the foundation for building a complete intelligent grievance management system.

---
