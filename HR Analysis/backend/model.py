import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

MODEL_PATH = "hr_model.pkl"

def train_initial_model():
    """Generates synthetic data and trains the baseline model."""
    np.random.seed(42)
    n = 2000
    data = {
        'tenure': np.random.randint(1, 15, n),
        'monthly_income': np.random.randint(2500, 18000, n),
        'last_rating': np.random.randint(1, 6, n),
        'engagement_score': np.random.uniform(1, 5, n),
        'distance_from_home': np.random.randint(1, 100, n),
        'overtime': np.random.randint(0, 2, n),
    }
    
    # Logic-based attrition probability
    prob = (
        (18000 - np.array(data['monthly_income'])) / 18000 * 0.4 +
        (5 - np.array(data['engagement_score'])) / 5 * 0.3 +
        np.array(data['overtime']) * 0.2 +
        np.array(data['distance_from_home']) / 100 * 0.1
    )
    y = (prob > 0.6).astype(int)
    X = pd.DataFrame(data)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

def get_model():
    if not os.path.exists(MODEL_PATH):
        return train_initial_model()
    return joblib.load(MODEL_PATH)

def predict_employee_risk(data_dict):
    model = get_model()
    # Convert dict to DataFrame
    features = ['tenure', 'monthly_income', 'last_rating', 'engagement_score', 'distance_from_home', 'overtime']
    input_df = pd.DataFrame([data_dict])[features]
    
    risk_prob = model.predict_proba(input_df)[0][1]
    
    # Recommendation Logic
    insights = []
    if data_dict['monthly_income'] < 5000:
        insights.append({"factor": "Low Income", "action": "Performance-based salary adjustment"})
    if data_dict['engagement_score'] < 3.0:
        insights.append({"factor": "Low Engagement", "action": "Manager check-in and mental health support"})
    if data_dict['overtime'] == 1:
        insights.append({"factor": "High Overtime", "action": "Workload redistribution or remote work option"})
    if data_dict['tenure'] > 4 and data_dict['last_rating'] > 4:
        insights.append({"factor": "Stagnation", "action": "Internal promotion or leadership training"})

    category = "Low"
    if risk_prob > 0.7: category = "High"
    elif risk_prob > 0.35: category = "Medium"
    
    return {
        "risk_score": float(risk_prob),
        "risk_category": category,
        "insights": insights
    }
