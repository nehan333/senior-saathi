contacts = []

def add_contact(name, phone):
    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)

    return {
        "message": "Contact added successfully",
        "contact": contact
    }


def get_contacts():
    return contacts


def send_emergency_alert():
    return {
        "message": "Emergency alert sent",
        "contacts": contacts
    }
