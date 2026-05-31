from fastapi import FastAPI, HTTPException
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


try:
    from reminder import add_reminder, get_reminders
    from family import (
        add_family_reminder,
        get_family_reminders,
        mark_reminder_missed,
    )
except ImportError:
    from backend.reminder import add_reminder, get_reminders
    from backend.family import (
        add_family_reminder,
        get_family_reminders,
        mark_reminder_missed,
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


class FamilyReminder(BaseModel):
    medicine: str
    time: str


def run_database_action(action):
    try:
        return action()
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {exc}",
        ) from exc


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
@app.post("/family/reminder")
def create_family_reminder(reminder: FamilyReminder):
    return run_database_action(
        lambda: add_family_reminder(
            reminder.medicine,
            reminder.time,
        )
    )


@app.get("/family/reminders")
def view_family_reminders():
    return run_database_action(get_family_reminders)


@app.put("/family/missed/{reminder_id}")
def mark_family_reminder_missed(reminder_id: int):
    return run_database_action(
        lambda: mark_reminder_missed(reminder_id)
    )
