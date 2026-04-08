# Predictive HR Analytics Platform

Welcome to the HR.INTEL Platform Prototype. This workspace contains a complete blueprint and practical example of an AI-driven turnover prediction system.

## 📂 Project Structure

- **`hr_analytics_platform_design.md`**: The architectural blueprint (Open this first!).
- **`predict_turnover.py`**: A working Python implementation using Random Forest and a Recommendation Engine.
- **`index.html` / `style.css` / `main.js`**: A premium, high-fidelity visual dashboard mockup.

## 🚀 How to Use

### 1. The ML Model
To run the turnover prediction script, ensure you have `pandas` and `scikit-learn` installed:
```bash
pip install pandas scikit-learn matplotlib
python predict_turnover.py
```
This script will:
1. Generate synthetic data for 1,000 employees.
2. Train a model to identify hidden attrition patterns.
3. Analyze a "High Risk" employee and generate a tailored retention strategy.

### 2. The Dashboard
Open `index.html` in any modern web browser to view the **HR.INTEL Vision**. 
- View organizational health metrics at a glance.
- Explore the "Critical Turnover Alerts" feed.
- Click **"Generate Strategy"** on any employee to see the AI-powered recommendation logic in action.

## 💡 Key Design Decisions
- **Black-Box to Glass-Box**: We don't just say *who* will leave; we explain *why* using primary driver flags.
- **Actionable Insights**: The system maps data points directly to management actions (e.g., salary vs market $\rightarrow$ increase pay).
- **Premium Aesthetics**: Designed with a "Global HR Leader" persona in mind—clean, dark, and focused on critical data.
