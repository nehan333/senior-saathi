try:
    from alerts import send_missed_reminder_alert
    from database import get_connection, init_db
except ImportError:
    from backend.alerts import send_missed_reminder_alert
    from backend.database import get_connection, init_db


def _row_to_reminder(row):
    return {
        "id": row[0],
        "senior_id": row[1],
        "created_by_user_id": row[2],
        "medicine": row[3],
        "reminder_time": row[4],
        "status": row[5],
        "created_at": row[6].isoformat() if row[6] else None,
    }


def _row_to_user(row):
    return {
        "id": row[0],
        "name": row[1],
        "phone": row[2],
        "role": row[3],
        "created_at": row[4].isoformat() if row[4] else None,
    }


def _row_to_family_member(row):
    return {
        "id": row[0],
        "senior_id": row[1],
        "senior_name": row[2],
        "family_member_id": row[3],
        "family_member_name": row[4],
        "relation": row[5],
        "created_at": row[6].isoformat() if row[6] else None,
    }


def add_user(name, phone, role):
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, phone, role)
        VALUES (%s, %s, %s)
        """,
        (name, phone, role),
    )

    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return {
        "message": "User added",
        "user": {
            "id": user_id,
            "name": name,
            "phone": phone,
            "role": role,
        },
    }


def get_users():
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, name, phone, role, created_at
        FROM users
        ORDER BY created_at DESC
        """
    )

    users = [_row_to_user(row) for row in cursor.fetchall()]
    cursor.close()
    conn.close()

    return users


def add_family_member(senior_id, family_member_id, relation):
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO family_members (senior_id, family_member_id, relation)
        VALUES (%s, %s, %s)
        """,
        (senior_id, family_member_id, relation),
    )

    conn.commit()
    member_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return {
        "message": "Family member linked",
        "family_member": {
            "id": member_id,
            "senior_id": senior_id,
            "family_member_id": family_member_id,
            "relation": relation,
        },
    }


def get_family_members():
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            fm.id,
            fm.senior_id,
            senior.name,
            fm.family_member_id,
            family.name,
            fm.relation,
            fm.created_at
        FROM family_members fm
        JOIN users senior ON senior.id = fm.senior_id
        JOIN users family ON family.id = fm.family_member_id
        ORDER BY fm.created_at DESC
        """
    )

    members = [_row_to_family_member(row) for row in cursor.fetchall()]
    cursor.close()
    conn.close()

    return members


def add_family_reminder(
    medicine, reminder_time, senior_id=None, created_by_user_id=None
):
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reminders
            (senior_id, created_by_user_id, medicine, reminder_time)
        VALUES (%s, %s, %s, %s)
        """,
        (senior_id, created_by_user_id, medicine, reminder_time),
    )

    conn.commit()
    reminder_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return {
        "message": "Family reminder added",
        "reminder": {
            "id": reminder_id,
            "senior_id": senior_id,
            "created_by_user_id": created_by_user_id,
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
        SELECT
            id,
            senior_id,
            created_by_user_id,
            medicine,
            reminder_time,
            status,
            created_at
        FROM reminders
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
        "UPDATE reminders SET status = %s WHERE id = %s",
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
        SELECT
            id,
            senior_id,
            created_by_user_id,
            medicine,
            reminder_time,
            status,
            created_at
        FROM reminders
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
