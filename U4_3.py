from multiprocessing import connection
import sqlite3


connection = sqlite3.connect('publ.db')
cursor = connection.cursor()
command = """
    CREATE TABLE IF NOT EXISTS tUsers(
        id INTEGER PRIMARY KEY,
        userName TEXT,
        age INTEGER,
        gender TEXT
    );
    """
cursor.execute(command)
command = """
    CREATE TABLE IF NOT EXISTS tPubl(
        id INTEGER PRIMARY KEY,
        id_user INTEGER,
        title TEXT,
        description TEXT,
        FOREIGN KEY (id_user) REFERENCES tUsers(id)
    );
    """
cursor.execute(command)
command = """
    CREATE TABLE IF NOT EXISTS tComments(
        id INTEGER PRIMARY KEY,
        textComm TEXT,
        id_user INTEGER,
        id_Publ INTEGER,
        FOREIGN KEY(id_user) REFERENCES tUsers(id),
        FOREIGN KEY(id_Publ) REFERENCES tPubl(id)
    );
    """
cursor.execute(command)
cursor.execute('INSERT INTO tUsers(id, userName, age, gender) VALUES(?, ?, ?, ?);', (5, 'Вася', 35, "М"))
cursor.execute('INSERT INTO tUsers(id, userName, age, gender) VALUES(?, ?, ?, ?);', (7, 'Маша', 40, 'Ж'))
cursor.execute('INSERT INTO tPubl(id, id_user, title, description) VALUES(?, ?, ?, ?);', (9, 2, 'Свойства камня', 'Всё о камнях'))
cursor.execute('INSERT INTO tComments(id, textComm, id_user, id_Publ) VALUES(?, ?, ?, ?);', (10, 'Занимательно!!!', 1, 1))
ans = cursor.execute("SELECT * FROM tComments WHERE (id = {})".format(1)).fetchall()
for i in ans:
    print(ans)
connection.commit()
cursor.close()
connection.close()
print('Соединение закрыто')
