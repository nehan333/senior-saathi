from fastapi import FastAPI
from pydantic import BaseModel
from backend.gov import get_schemes
from backend.reminder import add_reminder, get_reminders
from fastapi.middleware.cors import CORSMiddleware
from ai.ocr.ocr import extract_text
from backend.emergency import (
    add_contact,
    get_contacts,
    send_emergency_alert
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Reminder(BaseModel):
    medicine: str
    time: str

class Contact(BaseModel):
    name: str
    phone: str


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

@app.get("/schemes")
def schemes():
    return get_schemes()

@app.get("/ocr")
def ocr():
    text = extract_text("ai/ocr/sample.jpg")
    return {"text": text}

@app.post("/contacts")
def create_contact(contact: Contact):
    return add_contact(
        contact.name,
        contact.phone
    )


@app.get("/contacts")
def view_contacts():
    return get_contacts()


@app.post("/emergency")
def emergency():
    return send_emergency_alert()