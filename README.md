<<<<<<< Updated upstream
# Senior-Saathi — AI Civic & Daily Life Assistant for Elderly/Senior Citizens

## Overview

**Senior-Saathi** is an AI-powered multilingual assistant designed for **elderly, illiterate, and digitally excluded citizens**.

The platform aims to simplify access to:

* Government schemes and civic information
* Document understanding
* Multilingual communication
* Medicine reminders
* Accessibility-first digital interaction

Users can upload images of documents, extract text using OCR, translate content into their preferred language, access government welfare schemes, and manage medicine reminders.

This project is built as a modular platform intended to evolve from a working MVP into a scalable CivicTech accessibility solution.

---

## Problem Statement:-

Many elderly citizens face challenges with:

* Reading printed or digital documents
* Understanding government forms and notices
* Accessing digital services
* Language barriers
* Managing daily medicine schedules
* Using complex mobile or web applications

SeniorSaathi addresses these challenges through a simple and accessible interface.

---

## Features:-

### Document Reader (OCR)

Upload an image of:-

* Government notices
* Bills
* Medical prescriptions
* Printed documents

The system:-

* Detects text from images
* Extracts readable content
* Displays extracted information

---

### Multilingual Translation

Translate extracted content into multiple languages.

Current support:-

* English
* Telugu

Planned expansion:-

* Hindi
* Tamil
* Kannada
* Bengali
* Malayalam
* Marathi

---

### Voice Output:-

Generate spoken responses using Text-to-Speech.

The system can read translated text aloud to improve accessibility for:

* Elderly users
* Illiterate users
* Users with reading difficulties

---

### Government Scheme Assistant:-

Access information about welfare schemes.

Current version includes:-

* Old Age Pension
* Ayushman Bharat
* PM Kisan

Future versions will support:

* Smart eligibility filtering
* Scheme recommendations
* AI-powered civic assistant

---

### Medicine Reminder System

Manage simple medication reminders.

Users can:

* Add reminders
* View reminders
* Track medicine schedules

Future versions will support:

* Push notifications
* Family monitoring
* Daily health tracking

---

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* FastAPI
* Python
* MySQL

### AI / Processing

* EasyOCR
* Google Translate API Wrapper
* gTTS (Google Text-to-Speech)

### Development Tools

* GitLab
* Git
* Linux

---

## Project Structure

```text
SeniorSaathi/

frontend/
│
├── index.html
├── style.css
└── script.js

backend/
│
├── main.py
├── ocr.py
├── voice.py
├── gov.py
├── reminder.py
├── schemes.json
├── requirements.txt
└── venv/
```

---

## Installation

### Clone Repository

```bash
git clone YOUR_GITLAB_REPO_URL
```

Enter project directory:

```bash
cd SeniorSaathi
```

---

### Create Virtual Environment

Go to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Inside backend:

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Open frontend folder:

```bash
cd frontend
```

Launch:

```bash
xdg-open index.html
```

---

## API Endpoints

### Health Check

```http
GET /
```

---

### OCR Document Reader

```http
POST /read
```

Upload image file.

Returns extracted text.

---

### Translation

```http
POST /translate
```

Request:

```json
{
  "text":"Hello",
  "lang":"te"
}
```

---

### Voice Generation

```http
POST /speak
```

Generate audio response.

---

### Government Schemes

```http
GET /schemes
```

Retrieve scheme information.

---

### Add Reminder

```http
POST /reminder
```

Request:

```json
{
  "medicine":"BP Tablet",
  "time":"9 PM"
}
```

---

### View Reminders

```http
GET /reminders
```

---

## Team Workflow (GitLab)

### Clone Repository

```bash
git clone REPO_URL
```

---

### Create Feature Branch

Example:

```bash
git checkout -b frontend-ui
```

---

### Commit Changes

```bash
git add .
git commit -m "Completed feature"
```

---

### Push Branch

```bash
git push origin frontend-ui
```

---

### Create Merge Request

GitLab:

```text
Merge Requests → New Merge Request
```

Branch example:

```text
frontend-ui → main
```

---

### Pull Latest Changes

```bash
git checkout main
git pull origin main
```

Switch back:

```bash
git checkout your-branch
git merge main
```

---

## Development Roadmap

### Version 1 — MVP

Implemented:

* OCR document reading
* Translation
* Voice output
* Government schemes
* Medicine reminders
* Web frontend

---

### Version 2 — Product Upgrade

Planned:

* Better UI/UX
* Database integration
* User authentication
* Emergency contacts
* Improved accessibility

---

### Version 3 — AI Civic Platform

Planned:

* RAG Government Assistant
* Speech-to-Text
* Full multilingual support
* Smart scheme recommendation
* Family dashboard
* Mobile application

---

## Future Vision

SeniorSaathi is intended to become a complete accessibility-focused CivicTech platform helping elderly and illiterate citizens interact with:

* Government services
* Healthcare information
* Daily life management
* Digital systems

through voice, multilingual assistance, and simplified interfaces.

---

## Contributors

Team Members:

* Person 1 — Frontend
* Person 2 — OCR Module
* Person 3 — Voice & Translation
* Person 4 — Government Assistant
* Person 5 — Backend & Integration

---

## License

Academic / Internal Project.
=======
# Senior-Saathi — AI Civic & Daily Life Assistant for Elderly Citizens

## Overview

**Senior-Saathi** is an AI-powered multilingual assistant designed for **elderly, illiterate, and digitally excluded citizens**.

The platform aims to simplify access to:

* Government schemes and civic information
* Document understanding
* Multilingual communication
* Medicine reminders
* Accessibility-first digital interaction

Users can upload images of documents, extract text using OCR, translate content into their preferred language, access government welfare schemes, and manage medicine reminders.

This project is built as a modular platform intended to evolve from a working MVP into a scalable CivicTech accessibility solution.

---

## Problem Statement:-

Many elderly citizens face challenges with:

* Reading printed or digital documents
* Understanding government forms and notices
* Accessing digital services
* Language barriers
* Managing daily medicine schedules
* Using complex mobile or web applications

SeniorSaathi addresses these challenges through a simple and accessible interface.

---

## Features

### Document Reader (OCR)

Upload an image of:-

* Government notices
* Bills
* Medical prescriptions
* Printed documents

The system:-

* Detects text from images
* Extracts readable content
* Displays extracted information

---

### Multilingual Translation

Translate extracted content into multiple languages.

Current support:-

* English
* Telugu

Planned expansion:

* Hindi
* Tamil
* Kannada
* Bengali
* Malayalam
* Marathi

---

### Voice Output

Generate spoken responses using Text-to-Speech.

The system can read translated text aloud to improve accessibility for:

* Elderly users
* Illiterate users
* Users with reading difficulties

---

### Government Scheme Assistant

Access information about welfare schemes.

Current version includes:

* Old Age Pension
* Ayushman Bharat
* PM Kisan

Future versions will support:

* Smart eligibility filtering
* Scheme recommendations
* AI-powered civic assistant

---

### Medicine Reminder System

Manage simple medication reminders.

Users can:

* Add reminders
* View reminders
* Track medicine schedules

Future versions will support:

* Push notifications
* Family monitoring
* Daily health tracking

---

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* FastAPI
* Python

### AI / Processing

* EasyOCR
* Google Translate API Wrapper
* gTTS (Google Text-to-Speech)

### Development Tools

* GitLab
* Git
* Linux

---

## Project Structure

```text
SeniorSaathi/

frontend/
│
├── index.html
├── style.css
└── script.js

backend/
│
├── main.py
├── ocr.py
├── voice.py
├── gov.py
├── reminder.py
├── schemes.json
├── requirements.txt
└── venv/
```

---

## Installation

### Clone Repository

```bash
git clone YOUR_GITLAB_REPO_URL
```

Enter project directory:

```bash
cd SeniorSaathi
```

---

### Create Virtual Environment

Go to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Inside backend:

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Open frontend folder:

```bash
cd frontend
```

Launch:

```bash
xdg-open index.html
```

---

## API Endpoints

### Health Check

```http
GET /
```

---

### OCR Document Reader

```http
POST /read
```

Upload image file.

Returns extracted text.

---

### Translation

```http
POST /translate
```

Request:

```json
{
  "text":"Hello",
  "lang":"te"
}
```

---

### Voice Generation

```http
POST /speak
```

Generate audio response.

---

### Government Schemes

```http
GET /schemes
```

Retrieve scheme information.

---

### Add Reminder

```http
POST /reminder
```

Request:

```json
{
  "medicine":"BP Tablet",
  "time":"9 PM"
}
```

---

### View Reminders

```http
GET /reminders
```

---

## Team Workflow (GitLab)

### Clone Repository

```bash
git clone REPO_URL
```

---

### Create Feature Branch

Example:

```bash
git checkout -b frontend-ui
```

---

### Commit Changes

```bash
git add .
git commit -m "Completed feature"
```

---

### Push Branch

```bash
git push origin frontend-ui
```

---

### Create Merge Request

GitLab:

```text
Merge Requests → New Merge Request
```

Branch example:

```text
frontend-ui → main
```

---

### Pull Latest Changes

```bash
git checkout main
git pull origin main
```

Switch back:

```bash
git checkout your-branch
git merge main
```

---

## Development Roadmap

### Version 1 — MVP

Implemented:

* OCR document reading
* Translation
* Voice output
* Government schemes
* Medicine reminders
* Web frontend

---

### Version 2 — Product Upgrade

Planned:

* Better UI/UX
* Database integration
* User authentication
* Emergency contacts
* Improved accessibility

---

### Version 3 — AI Civic Platform

Planned:

* RAG Government Assistant
* Speech-to-Text
* Full multilingual support
* Smart scheme recommendation
* Family dashboard
* Mobile application

---

## Future Vision

SeniorSaathi is intended to become a complete accessibility-focused CivicTech platform helping elderly and illiterate citizens interact with:

* Government services
* Healthcare information
* Daily life management
* Digital systems

through voice, multilingual assistance, and simplified interfaces.

---

## Contributors

Team Members:

* Person 1 — Frontend
* Person 2 — OCR Module
* Person 3 — Voice & Translation
* Person 4 — Government Assistant
* Person 5 — Backend & Integration

---

## License

Academic / Internal Project.
>>>>>>> Stashed changes
