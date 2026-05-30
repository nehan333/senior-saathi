reminders = []

def add_reminder(medicine, time):
    reminder = {
        "medicine": medicine,
        "time": time
    }

    reminders.append(reminder)

    return {}
        "message": "Reminder added successfully",
        "reminder": reminder
    }

def get_reminders():
    return reminders