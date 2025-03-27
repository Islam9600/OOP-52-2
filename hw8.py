import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Создание таблицы users (если ее нет)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
""")

# Вставка тестовых данных (если таблица пустая)
cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO users (name, age, grade) VALUES ('Islam', 18, 'A')")
    cursor.execute("INSERT INTO users (name, age, grade) VALUES ('Alim', 17, 'B')")
    conn.commit()

# Создание представления users_grade
cursor.execute("""
    CREATE VIEW IF NOT EXISTS users_grade AS
    SELECT id, name, age, grade FROM users
""")

conn.commit()
conn.close()

# Функция для получения данных из представления
def get_young_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users_grade")
    results = cursor.fetchall()

    conn.close()
    return results

print(get_young_users())
