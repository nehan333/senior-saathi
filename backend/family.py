try:
    from database import get_connection, init_db
    from alerts import send_missed_reminder_alert
except ImportError:
    from backend.database import get_connection, init_db
    from backend.alerts import send_missed_reminder_alert


def _row_to_reminder(row):
    return {
        "id": row[0],
        "medicine": row[1],
        "reminder_time": row[2],
        "status": row[3],
        "created_at": row[4].isoformat() if row[4] else None,
    }


def add_family_reminder(medicine, reminder_time):
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO family_reminders (medicine, reminder_time)
        VALUES (%s, %s)
        """,
        (medicine, reminder_time),
    )

    conn.commit()
    reminder_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return {
        "message": "Family reminder added",
        "reminder": {
            "id": reminder_id,
            "medicine": medicine,
            "reminder_time": reminder_time,
            "status": "pending",
        },
    }


def get_family_reminders():
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, medicine, reminder_time, status, created_at
        FROM family_reminders
        ORDER BY created_at DESC
        """
    )

    reminders = [_row_to_reminder(row) for row in cursor.fetchall()]
    cursor.close()
    conn.close()

    return reminders


def mark_reminder_missed(reminder_id):
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE family_reminders SET status = %s WHERE id = %s",
        ("missed", reminder_id),
    )
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return {
            "message": "Reminder not found",
            "id": reminder_id,
        }

    cursor.execute(
        """
        SELECT id, medicine, reminder_time, status, created_at
        FROM family_reminders
        WHERE id = %s
        """,
        (reminder_id,),
    )
    reminder = _row_to_reminder(cursor.fetchone())

    cursor.close()
    conn.close()

    return {
        "message": "Reminder marked missed",
        "alert": send_missed_reminder_alert(reminder),
    }
