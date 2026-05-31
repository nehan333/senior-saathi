import os


def get_connection():
    try:
        import mysql.connector
    except ImportError as exc:
        raise RuntimeError(
            "mysql-connector-python is not installed. Run: pip install mysql-connector-python"
        ) from exc

    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "senioruser"),
        password=os.getenv("MYSQL_PASSWORD", "password123"),
        database=os.getenv("MYSQL_DATABASE", "seniorsaathi"),
    )


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS family_reminders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            medicine VARCHAR(255) NOT NULL,
            reminder_time VARCHAR(50) NOT NULL,
            status VARCHAR(50) NOT NULL DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    cursor.close()
    conn.close()
