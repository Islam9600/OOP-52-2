import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute('''
    CREATE TABLE users(
        name VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()


def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен!")


def get_user_by_id(rowid):
    cursor.execute("SELECT name, age, hobby FROM users WHERE rowid = ?", (rowid,))
    user = cursor.fetchone()

    if user:
        print(f"NAME: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")
    else:
        print(f"Пользователь с rowid {rowid} не найден.")


def update_users(rowid, name=None, age=None, hobby=None):
    updates = []
    values = []

    if name:
        updates.append("name = ?")
        values.append(name)
    if age:
        updates.append("age = ?")
        values.append(age)
    if hobby:
        updates.append("hobby = ?")
        values.append(hobby)

    if updates:
        values.append(rowid)
        query = f"UPDATE users SET {', '.join(updates)} WHERE rowid = ?"
        cursor.execute(query, values)
        connect.commit()
        print(f"Пользователь с rowid {rowid} обновлён.")
    else:
        print("Нет данных для обновления.")


add_user('Бекс', 23, 'Плавать')
add_user('Ислам', 25, 'Чтение')
add_user('Амина', 30, 'Танцы')
add_user('Муха', 27, 'Футбол')

get_user_by_id(1)
get_user_by_id(2)
get_user_by_id(3)
get_user_by_id(4)
update_users(1, name="Oleg")
get_user_by_id(1)

connect.close()
