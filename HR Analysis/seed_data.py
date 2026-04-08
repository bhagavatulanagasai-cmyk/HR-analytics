import requests
import json
import time

URL = "http://localhost:8000/api/predict"

SAMPLES = [
    {"name": "Sarah Jenkins", "department": "Engineering", "tenure": 5, "monthly_income": 12000, "last_rating": 5, "engagement_score": 4.8, "distance_from_home": 10, "overtime": 0},
    {"name": "Michael Ross", "department": "Sales", "tenure": 3, "monthly_income": 4500, "last_rating": 3, "engagement_score": 2.1, "distance_from_home": 45, "overtime": 1},
    {"name": "Emily Zhao", "department": "Product", "tenure": 1, "monthly_income": 9000, "last_rating": 4, "engagement_score": 3.2, "distance_from_home": 5, "overtime": 0},
    {"name": "David Miller", "department": "IT", "tenure": 8, "monthly_income": 6000, "last_rating": 2, "engagement_score": 1.5, "distance_from_home": 20, "overtime": 1},
    {"name": "Anna Schmidt", "department": "Engineering", "tenure": 4, "monthly_income": 8500, "last_rating": 4, "engagement_score": 4.5, "distance_from_home": 12, "overtime": 0}
]

def seed():
    print("Seeding sample data to HR.INTEL...")
    for sample in SAMPLES:
        try:
            res = requests.post(URL, json=sample)
            if res.status_code == 200:
                print(f"Added {sample['name']}")
            else:
                print(f"Failed to add {sample['name']}")
        except Exception as e:
            print(f"Server not reachable yet. Start the backend first! Error: {e}")
            break

if __name__ == "__main__":
    seed()
