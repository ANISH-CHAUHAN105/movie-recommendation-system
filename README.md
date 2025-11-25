# 🎬 Content-Based Movie Recommendation System

A lightweight, TF-IDF–powered movie recommender built with Streamlit. The application analyzes textual metadata to identify movies most similar to a title provided by the user.

## 🚀 Key Features
- Content-based recommendations using TF-IDF and cosine similarity  
- Streamlit interface for quick interaction  
- Minimal, readable codebase suitable for learning  
- Straightforward deployment on Streamlit Community Cloud  

## 🧠 Methodology
1. Movie metadata is combined into a single descriptive text field.  
2. TF-IDF vectorization converts the text into numerical feature vectors.  
3. Cosine similarity scores are computed across all movies.  
4. The system retrieves the closest matches to the requested title.  

This avoids reliance on user ratings or collaborative filtering and remains effective even for rarely rated films.

## 📁 Project Structure
.
├── app.py
├── data/
│ └── movies.csv
├── requirements.txt
└── README.md

## ▶️ Running Locally
Install dependencies and launch the interface:
```bash
pip install -r requirements.txt
streamlit run app.py
