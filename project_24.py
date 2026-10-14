import sqlite3


def create_database(connection):
    connection.execute("CREATE TABLE IF NOT EXISTS tasks "
                       "(id INTEGER PRIMARY KEY, title TEXT NOT NULL)")


def main():
    with sqlite3.connect(":memory:") as connection:
        create_database(connection)
        connection.execute("INSERT INTO tasks(title) VALUES (?)", ("Study Python",))
        tasks = connection.execute("SELECT id, title FROM tasks").fetchall()
        print(tasks)


if __name__ == "__main__":
    main()
