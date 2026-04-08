from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
import os

from database import init_db, add_employee, get_all_employees
from model import predict_employee_risk

app = FastAPI(title="HR.INTEL Predictive API")

# Initialize Database
init_db()

# Models
class EmployeeInput(BaseModel):
    name: str
    department: str
    tenure: int
    monthly_income: float
    last_rating: int
    engagement_score: float
    distance_from_home: float
    overtime: int

@app.post("/api/predict")
async def predict(emp: EmployeeInput):
    try:
        data_dict = emp.dict()
        results = predict_employee_risk(data_dict)
        
        # Save to DB
        full_data = {**data_dict, **results}
        emp_id = add_employee(full_data)
        
        return {"id": emp_id, **results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/employees")
async def list_employees():
    return get_all_employees()

# Mount Frontend Static Files
# We assume the index.html is in the ../frontend directory
if os.path.exists("../frontend"):
    app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
