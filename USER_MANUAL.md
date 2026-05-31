# SeniorSaathi User Manual

## Introduction

SeniorSaathi is an AI-powered assistant designed to help senior citizens access government schemes, read documents using OCR, translate content, and manage reminders.

## Features

### Government Schemes

* View available government schemes.
* Read scheme information aloud.

### OCR Document Reader

* Upload an image document.
* Extract text automatically.
* Read extracted text aloud.

### Translation

* Translate extracted text into supported languages.
* Supports regional language accessibility.

### Reminders

* Create medicine reminders.
* View reminder schedules.

### Emergency Contacts

* Store emergency contacts.
* Trigger emergency alerts.

## Running the Project

```bash
uv pip install -r requirements.txt
python -m uvicorn backend.main:app --reload
```

Frontend:

Open:

```text
frontend/index.html
```

in a browser.
