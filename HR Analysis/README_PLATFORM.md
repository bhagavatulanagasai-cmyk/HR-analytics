# HR.INTEL | Production-Ready Predictive HR Analytics

A complete end-to-end platform for predicting employee turnover risk using Machine Learning (Random Forest) and a React-based professional dashboard.

## 🚀 Features
- **Real-time Prediction**: Submit employee data and get immediate risk probability.
- **Explainable Insights**: See exactly *why* an employee is high-risk (e.g., Salary vs Market, Overtime).
- **Retention Strategies**: AI-generated action plans for each employee.
- **Interactive Dashboard**: Modern, glassmorphic UI with organizational health KPIs.

## 🛠 Tech Stack
- **Backend**: Python 3.13, FastAPI, SQLite, Scikit-Learn.
- **Frontend**: React 18, Tailwind CSS (Modern Single-Page App).
- **ML Engine**: Random Forest Classifier with synthetic data pre-training.

## 📦 Project Structure
```text
/backend
  main.py       # FastAPI API & Static Server
  model.py      # ML Engine & Logic
  database.py   # SQLite Operations
/frontend
  index.html    # React/Tailwind SPA
seed_data.py    # Sample data injector
```

## 🏁 How to Run

### 1. Install Dependencies
Ensure you have the required Python packages:
```bash
pip install fastapi uvicorn pandas scikit-learn joblib requests
```

### 2. Start the Backend
Navigate to the `backend` directory and run the server:
```bash
cd backend
python main.py
```
*The server will start at `http://localhost:8000`.*

### 3. Seed Sample Data (Optional)
While the server is running, open a new terminal and run:
```bash
python seed_data.py
```

### 4. Access the Platform
Open your browser and go to:
**[http://localhost:8000](http://localhost:8000)**

---
*Designed with ❤️ by Antigravity AI*
