import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
# import matplotlib.pyplot as plt

# 1. Generate Synthetic Data
def generate_hr_data(n=1000):
    np.random.seed(42)
    data = {
        'Tenure': np.random.randint(1, 10, n),
        'MonthlyIncome': np.random.randint(3000, 15000, n),
        'LastReviewRating': np.random.randint(1, 6, n),
        'EngagementScore': np.random.randint(1, 6, n),
        'DistanceFromHome': np.random.randint(1, 50, n),
        'YearsSinceLastPromotion': np.random.randint(0, 10, n),
        'Overtime': np.random.choice(['Yes', 'No'], n),
        'Department': np.random.choice(['Sales', 'R&D', 'HR', 'IT'], n)
    }
    
    # Logic for attrition (target)
    # Higher risk if low income, high distance, low engagement, and lots of overtime
    attrition_prob = (
        (15000 - np.array(data['MonthlyIncome'])) / 15000 * 0.4 +
        np.array(data['DistanceFromHome']) / 50 * 0.2 +
        (5 - np.array(data['EngagementScore'])) / 5 * 0.3 +
        (np.array(data['Overtime']) == 'Yes').astype(int) * 0.1
    )
    data['Attrition'] = (attrition_prob > 0.6).astype(int)
    
    return pd.DataFrame(data)

# 2. Preprocess Data
df = generate_hr_data()
le = LabelEncoder()
df['Overtime'] = le.fit_transform(df['Overtime'])
df['Department_Enc'] = le.fit_transform(df['Department'])

X = df.drop(['Attrition', 'Department'], axis=1)
y = df['Attrition']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Feature Importance
importances = model.feature_importances_
feature_names = X.columns
feat_importances = pd.Series(importances, index=feature_names)
print("\n--- Key Factors Driving Turnover ---")
print(feat_importances.sort_values(ascending=False))

# 5. Prediction and Recommendation Engine
def get_recommendation(employee_data):
    risk_score = model.predict_proba(employee_data)[0][1]
    
    print(f"\nEmployee Turnover Risk Score: {risk_score:.2f}")
    
    if risk_score > 0.7:
        print("Category: [HIGH RISK] - Immediate Intervention Needed")
        
        # Simple logic-based recommendations
        if employee_data['MonthlyIncome'].values[0] < 5000:
            return "Recommendation: Priority 1 - Salary Review. Income is below threshold."
        elif employee_data['YearsSinceLastPromotion'].values[0] > 3:
            return "Recommendation: Priority 1 - Career Growth Chat. Promotion is overdue."
        elif employee_data['EngagementScore'].values[0] < 3:
            return "Recommendation: Priority 1 - Manager 1:1. Engagement is low."
        else:
            return "Recommendation: Review Work-Life Balance and Overtime status."
    
    elif risk_score > 0.3:
        return "Category: [MEDIUM RISK] - Schedule a check-in."
    else:
        return "Category: [LOW RISK] - Maintain current engagement."

# Example: A high-risk employee profile
new_employee = pd.DataFrame([{
    'Tenure': 5,
    'MonthlyIncome': 3500,
    'LastReviewRating': 4,
    'EngagementScore': 2,
    'DistanceFromHome': 45,
    'YearsSinceLastPromotion': 4,
    'Overtime': 1, # Yes
    'Department_Enc': 1 # R&D
}])

print("\n--- Individual Assessment for Employee #402 ---")
print(get_recommendation(new_employee))
