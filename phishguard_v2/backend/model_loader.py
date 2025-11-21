
import joblib
import pandas as pd
import numpy as np
from feature_extractor import extract_features

model = joblib.load("xgb_model.pkl")
feature_columns = ["url_length", "has_https", "special_char_count",
                   "suspicious_keyword", "subdomain_depth", "has_ip"]

def predict_url(url):
    # 1️⃣ Extract numeric features from URL
    features = extract_features(url)  # e.g., [18, 1, 4, 0, 0, 0]

    # 2️⃣ Convert to DataFrame or 2D array for model
    fv_df = pd.DataFrame([features], columns=feature_columns)  # 1 row, N columns

    # 3️⃣ Get probability from ML model
    prob = float(model.predict_proba(fv_df)[0][1])  # probability URL is phishing

    # 4️⃣ Map probability to human-readable label
    if prob < 0.4:
        label = "SAFE 🟢"
    elif prob < 0.7:
        label = "SUSPICIOUS 🟡"
    else:
        label = "PHISHING 🔴"

    return prob, label

