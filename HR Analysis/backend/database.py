import sqlite3
import pandas as pd
import json

DB_NAME = "hr_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT,
            tenure INTEGER,
            monthly_income REAL,
            last_rating INTEGER,
            engagement_score REAL,
            distance_from_home REAL,
            overtime INTEGER,
            risk_score REAL,
            risk_category TEXT,
            insights TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_employee(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (
            name, department, tenure, monthly_income, last_rating, 
            engagement_score, distance_from_home, overtime, 
            risk_score, risk_category, insights
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['name'], data['department'], data['tenure'], data['monthly_income'],
        data['last_rating'], data['engagement_score'], data['distance_from_home'],
        data['overtime'], data['risk_score'], data['risk_category'], 
        json.dumps(data['insights'])
    ))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_all_employees():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM employees", conn)
    conn.close()
    # Parse insights JSON back to list
    employees = df.to_dict('records')
    for emp in employees:
        emp['insights'] = json.loads(emp['insights']) if emp['insights'] else []
    return employees
