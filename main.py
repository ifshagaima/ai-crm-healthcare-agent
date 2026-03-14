from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model for interaction
class Interaction(BaseModel):
    doctor_name: str
    hospital: str
    notes: str


# Home API
@app.get("/")
def home():
    return {"message": "AI CRM System Running"}


# Tool 1: Log Interaction
@app.post("/log_interaction")
def log_interaction(data: Interaction):
    return {
        "status": "Interaction logged successfully",
        "doctor": data.doctor_name,
        "hospital": data.hospital,
        "notes": data.notes
    }


# Tool 2: Edit Interaction
@app.put("/edit_interaction")
def edit_interaction(data: Interaction):
    return {
        "status": "Interaction updated successfully",
        "doctor": data.doctor_name,
        "hospital": data.hospital,
        "notes": data.notes
    }


# Tool 3: View Interaction History
@app.get("/interaction_history")
def interaction_history():
    return {
        "history": [
            {
                "doctor": "Dr Sharma",
                "hospital": "Apollo Hospital",
                "notes": "Discussed diabetes medicine"
            },
            {
                "doctor": "Dr Kumar",
                "hospital": "Fortis Hospital",
                "notes": "Talked about insulin product"
            }
        ]
    }
# Tool 4: Schedule Follow-up
@app.post("/schedule_followup")
def schedule_followup(doctor_name: str, date: str):
    return {
        "status": "Follow-up scheduled",
        "doctor": doctor_name,
        "date": date
    }