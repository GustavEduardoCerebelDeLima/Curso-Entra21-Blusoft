# import sqlite3

connection = sqlite3.connect('Database.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clients('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'cpf TEXT,'
               'name TEXT,'
               'birth_date TEXT,'
               'cep TEXT,'
               'weight REAL,'
               'height REAL)')

connection.commit()


cpf = input('type the cpf: ')
name = input('type the name: ')
birth_date = input('type the birth date: ')
cep = input('type the cep: ')
weight = float(input('type the weight: '))
height = float(input('type the height: '))

cursor.execute('INSERT INTO clients (cpf, name, birth_date, cep, weight, height)'
               'VALUES(?, ?, ?, ?, ?,?)', (cpf, name, birth_date, cep, weight, height))


cursor.execute('SELECT * FROM clients')
for client in cursor.fetchall():
    print(f'{client[0]} - {client[1]} - {client[2]} - {client[3]} - {client[4]} - {client[5]}')


cursor.close()
connection.close()


