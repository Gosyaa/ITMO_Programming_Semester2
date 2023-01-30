import sqlite3

try:
    connection = sqlite3.connect('city.db')
    cursor = connection.cursor()

    select_query = """
    CREATE TABLE IF NOT EXISTS city(Номер INT, Имя города TEXT);
    """
    cursor.execute(select_query)
    cities = []
    cities.append((1, 'Москва'))
    cities.append((2, "Санк-Петербург"))
    cities.append((3, 'Париж'))
    cities.append((4, 'Лондон'))
    cities.append((5, 'Берлин'))
    cities.append((6, 'Варшава'))
    cities.append((7, 'Киев'))
    cities.append((8, 'Афины'))
    cities.append((9, 'Прага'))
    cities.append((10, 'Саратов'))
    cursor.executemany('INSERT INTO city VALUES(?, ?);', cities)
except sqlite3.Error as error:
    print('Ошибка')
finally:
    if connection:
        cursor.execute('SELECT * FROM city')
        ans = cursor.fetchmany(10)
        for i in ans:
            print(i[0], i[1])
        connection.commit()
        cursor.close()
        connection.close()
        print('Соединение закрыто')