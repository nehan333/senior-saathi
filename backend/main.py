<<<<<<< Updated upstream
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.gov import get_schemes
#from backend.translation import translate_text
from backend.reminder import add_reminder, get_reminders
from fastapi.middleware.cors import CORSMiddleware
from ai.ocr.ocr import extract_text
# from backend.emergency import (
#    add_contact,
#    get_contacts,
#    send_emergency_alert
#)


try:
    from reminder import add_reminder, get_reminders
    from family import (
        add_family_reminder,
        add_family_member,
        add_user,
        get_family_members,
        get_family_reminders,
        get_users,
        mark_reminder_missed,
    )
except ImportError:
    from backend.reminder import add_reminder, get_reminders
    from backend.family import (
        add_family_reminder,
        add_family_member,
        add_user,
        get_family_members,
        get_family_reminders,
        get_users,
        mark_reminder_missed,
    )
from fastapi import UploadFile, File
import shutil

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
    senior_id: int | None = None
    created_by_user_id: int | None = None


class UserRequest(BaseModel):
    name: str
    phone: str | None = None
    role: str


class FamilyMemberRequest(BaseModel):
    senior_id: int
    family_member_id: int
    relation: str | None = None


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

@app.get("/schemes")
def schemes():
    return get_schemes()

'''app.post("/ocr")
async def ocr(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    return {"text": text}'''

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
@app.post("/family/user")
def create_family_user(user: UserRequest):
    return run_database_action(
        lambda: add_user(
            user.name,
            user.phone,
            user.role,
        )
    )


@app.get("/family/users")
def view_family_users():
    return run_database_action(get_users)


@app.post("/family/member")
def create_family_member(member: FamilyMemberRequest):
    return run_database_action(
        lambda: add_family_member(
            member.senior_id,
            member.family_member_id,
            member.relation,
        )
    )


@app.get("/family/members")
def view_family_members():
    return run_database_action(get_family_members)


@app.post("/family/reminder")
def create_family_reminder(reminder: FamilyReminder):
    return run_database_action(
        lambda: add_family_reminder(
            reminder.medicine,
            reminder.time,
            reminder.senior_id,
            reminder.created_by_user_id,
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
    
    

from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    language: str

@app.post("/translate")
def translate(req: TranslationRequest):
    translated = translate_text(
        req.text,
        req.language
    )

    return {
        "translated": translated
    }
=======
from fastapi import FastAPI
from pydantic import BaseModel
from backend.gov import get_schemes
from backend.reminder import add_reminder, get_reminders
from fastapi.middleware.cors import CORSMiddleware
from ai.ocr.ocr import extract_text


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
>>>>>>> Stashed changes
