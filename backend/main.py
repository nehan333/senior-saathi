from fastapi import FastAPI
from pydantic import BaseModel

from reminder import add_reminder, get_reminders

app = FastAPI()


class Reminder(BaseModel):
    medicine: str
    time: str


@app.get("/")
def home():
    return {
        "message": "SeniorSaathi API Running"
    }


@app.post("/reminder")
def create_reminder(reminder: Reminder):
    return add_reminder(
        reminder.medicine,
        reminder.time
    )


@app.get("/reminders")
def view_reminders():
    return get_reminders()