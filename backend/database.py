import os


def get_connection():
    try:
        import mysql.connector
    except ImportError as exc:
        raise RuntimeError(
            "mysql-connector-python is not installed. "
            "Run: pip install mysql-connector-python"
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
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(30),
            role VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS family_members (
            id INT AUTO_INCREMENT PRIMARY KEY,
            senior_id INT NOT NULL,
            family_member_id INT NOT NULL,
            relation VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (senior_id) REFERENCES users(id),
            FOREIGN KEY (family_member_id) REFERENCES users(id)
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS reminders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            senior_id INT,
            created_by_user_id INT,
            medicine VARCHAR(255) NOT NULL,
            reminder_time VARCHAR(50) NOT NULL,
            status VARCHAR(50) NOT NULL DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (senior_id) REFERENCES users(id),
            FOREIGN KEY (created_by_user_id) REFERENCES users(id)
        )
        """
    )

    conn.commit()
    cursor.close()
    conn.close()
