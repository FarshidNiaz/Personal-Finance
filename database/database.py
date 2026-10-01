import sqlite3
from pathlib import Path


# مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# مسیر دیتابیس
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "finance.db"


def get_connection():
    DATA_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DB_PATH)

    return connection


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()

    # =========================
    # تراکنش‌ها
    # =========================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_type TEXT NOT NULL,
            amount INTEGER NOT NULL,
            category TEXT,
            description TEXT,
            transaction_date TEXT NOT NULL
        )
    """)

    # =========================
    # دارایی‌ها
    # =========================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            asset_type TEXT,
            amount INTEGER DEFAULT 0,
            description TEXT
        )
    """)

    # =========================
    # بدهی‌ها
    # =========================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS liabilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount INTEGER NOT NULL,
            description TEXT
        )
    """)

    # =========================
    # اهداف مالی
    # =========================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS financial_goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            target_amount INTEGER NOT NULL,
            current_amount INTEGER DEFAULT 0,
            target_date TEXT,
            description TEXT
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":

    create_tables()

    print("Database created successfully!")
    print(f"Database path: {DB_PATH}")