import streamlit as st
import joblib
from transformers import pipeline
import re

# Page config
st.set_page_config(page_title="AI Grievance System", layout="centered")

# Load models
tfidf = joblib.load('model/tfidf_vectorizer.pkl')
dept_model = joblib.load('model/department_model.pkl')

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# Prediction function
def predict(text):
    cleaned = clean_text(text)
    vec = tfidf.transform([cleaned])

    dept = dept_model.predict(vec)[0]

    sentiment_raw = sentiment_pipeline(text[:512])[0]['label']
    sentiment = "Positive" if sentiment_raw == "POSITIVE" else "Negative"

    priority = 3 if sentiment == "Negative" else 1
    confidence = dept_model.predict_proba(vec).max()

    return dept, sentiment, priority, round(float(confidence), 2)

# Priority color
def priority_badge(priority):
    if priority == 3:
        return "🔴 High"
    elif priority == 2:
        return "🟡 Medium"
    else:
        return "🟢 Low"

# ---------------- UI ---------------- #

st.title("🏛️ AI-Powered Grievance System")
st.markdown("### 🚀 Smart Complaint Classification & Priority Detection")

st.divider()

# Sidebar
st.sidebar.header("📌 Quick Examples")
example = st.sidebar.selectbox(
    "Try an example:",
    [
        "",
        "Water supply not available for 3 days",
        "Roads are damaged and unsafe",
        "Electricity is fluctuating frequently",
        "Garbage is not collected regularly"
    ]
)

# Input box
user_input = st.text_area("📝 Enter your complaint:", value=example, height=120)

# Button
if st.button("🔍 Analyze Complaint"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a complaint")
    else:
        dept, sentiment, priority, confidence = predict(user_input)

        st.success("✅ Analysis Complete")

        # Results in columns
        col1, col2 = st.columns(2)

        with col1:
            st.metric("🏢 Department", dept)
            st.metric("😊 Sentiment", sentiment)

        with col2:
            st.metric("⚡ Priority", priority_badge(priority))
            st.metric("📊 Confidence", f"{confidence*100}%")

        st.progress(confidence)

        st.divider()

        # Insight section
        st.markdown("### 🧠 Insight")
        if priority == 3:
            st.error("🚨 This issue requires immediate attention!")
        elif priority == 2:
            st.warning("⚠️ Moderate priority complaint.")
        else:
            st.info("ℹ️ Low priority complaint.")

# Footer
st.divider()
st.caption("Built with ❤️ using ML + BERT + Streamlit")