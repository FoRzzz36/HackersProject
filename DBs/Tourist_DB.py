import sqlite3
connection = sqlite3.connect("TouristBotStatistics.db")
connection.execute("PRAGMA Journal_mode=WAL")
cursor = connection.cursor()
def CityCode(s):
    if s == 'klgd':
        return('Калининград ')
    if s == 'zel':
        return('Зеленоградск')
    if s == 'sve':
        return('Светлогорск ')
    if s == 'yant':
        return('Янтарный    ')
    if s == 'pol':
        return('Полесск     ')
    if s == 'cher':
        return('Черняховск  ')
#таблица visit
def add_visitor(s): #добавть посетителя
    cursor.execute('SELECT count FROM visit WHERE location = ?', (s, ))
    users = cursor.fetchone()
    cursor.execute('UPDATE visit SET count = ? WHERE location = ?', (int(users[0]) + 1, s))
    connection.commit()
def print_visit(): #вывести всё из visit
    cursor.execute('SELECT * FROM visit')
    users = cursor.fetchall()
    for user in users:
        print(user)
#таблица places
def change_sale(id, s):
    try:
        cursor.execute('UPDATE places SET sale = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_name(id, s):
    try:
        cursor.execute('SELECT * FROM visit')
        res = cursor.fetchall()
        cursor.execute('SELECT Name FROM places WHERE id = ?', (id, ))
        a = cursor.fetchone()
        k = a[0] #имя с данным id
        cursor.execute('SELECT City FROM places WHERE id = ?', (id, ))
        b = cursor.fetchone()
        m = b[0] #код города с данным id
        for r in res:
            t = r[0]
            if t[0: len(t) - 15] == k and t[len(t)-13:len(t)-1] == CityCode(m):
                d = t.replace(k, s)
                cursor.execute('UPDATE visit SET location = ? WHERE location = ?', (d, r[0]))
        cursor.execute('UPDATE places SET Name = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_address(id, s):
    try:
        cursor.execute('UPDATE places SET Address = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_desc(id, s):
    try:
        cursor.execute('UPDATE places SET desc = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_link(id, s):
    try:
        cursor.execute('UPDATE places SET link = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_city(id, s):
    try:
        cursor.execute('SELECT * FROM visit')
        res = cursor.fetchall()
        cursor.execute('SELECT Name FROM places WHERE id = ?', (id, ))
        a = cursor.fetchone()
        k = a[0] #имя с данным id
        cursor.execute('SELECT City FROM places WHERE id = ?', (id, ))
        b = cursor.fetchone()
        m = b[0] #код города с данным id
        for r in res:
            t = r[0]
            if t[0: len(t) - 15] == k and t[len(t)-13:len(t)-1] == CityCode(m):
                d = t.replace(CityCode(m), CityCode(s))
                cursor.execute('UPDATE visit SET location = ? WHERE location = ?', (d, r[0]))
        cursor.execute('UPDATE places SET City = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def change_type(id, s):
    try:
        cursor.execute('UPDATE places SET type = ? WHERE id = ?', (s, id))
        connection.commit()
    except ValueError:
        pass
def print_places():
    cursor.execute('SELECT * FROM places')
    users = cursor.fetchall()
    for user in users:
        print(user)
#таблица rating
def print_rating():
    cursor.execute('SELECT * FROM rating')
    users = cursor.fetchall()
    for user in users:
        print(user)
def Insert_rating(i):
    cursor.execute('SELECT number FROM rating WHERE rtng = ?', (i, ))
    res = cursor.fetchone()
    cursor.execute('UPDATE rating SET number = ? WHERE rtng = ?', (int(res[0]) + 1, i))
    connection.commit()
def output():
    connection.close()
change_name(39, 'abcdefg')
change_city(41, 'zel')
print_places()
print_visit()