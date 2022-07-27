# import sqlite3

# connection = sqlite3.connect('My first datbase.db')
# cursor = connection.cursor()

# # CREATE THE TABLE
# cursor.execute('CREATE TABLE IF NOT EXISTS Fruits('
#                'ID_fruit INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'fruit_name TEXT,'
#                'variety TEXT)')
#
# connection.commit()

# insert data in the table
# cursor.execute('INSERT INTO Fruits('
#                'fruit_name, variety)'
#                'VALUES ("Banana", "Caturra")')
#
# connection.commit()

# # update register
# cursor.execute('UPDATE Fruits SET variety = "Prata" WHERE ID_fruit=3')
# connection.commit()

# # seek database
# cursor.execute('SELECT * FROM Fruits')
# for fruit in cursor.fetchall():
#     print(f'{fruit[0]} - {fruit[1]} - {fruit[2]}')

# delete
# cursor.execute('DELETE FROM Fruits WHERE ID_fruit=1')
# connection.commit()

# delete the table
# cursor.execute('DROP TABLE Fruits')
# connection.commit()
#
#
# cursor.close()
# connection.close()
