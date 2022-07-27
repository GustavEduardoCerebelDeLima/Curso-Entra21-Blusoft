import sqlite3

connection = sqlite3.connect('Database_pokemon.db')
cursor = connection.cursor()
print('connection successfully')

pokemons_list = []


def create():
    name = input('type the name: ')
    kind = input('type the type: ')
    pokedex = input('type the pokedex: ')
    level = float(input('type the level: '))
    cursor.execute('INSERT INTO pokemons_list('
                   'name, type, pokedex, level)'
                   'VALUES (?, ?, ?, ?)', (name, kind, pokedex, level))
    connection.commit()


def buff_up():
    level = input('type the new level: ')
    id = int(input('type the id of the pokemon you want to buff up: '))
    cursor.execute(f'UPDATE pokemons_list SET level = {level} + 1 WHERE id={id}')
    connection.commit()


def edit():
    option = int(input('what do you want to edit [1] name [2] kind [3] pokedex [4] level:'))
    if option == 1:
        name = input('type the new name: ')
        id = int(input('type the id of the pokemon you want to edit: '))
        cursor.execute(f'UPDATE pokemons_list SET name = "{name}" WHERE id={id}')
        connection.commit()
    elif option == 2:
        kind = input('type the new kind: ')
        id = int(input('type the id of the pokemon you want to edit: '))
        cursor.execute(f'UPDATE pokemons_list SET kind = "{kind}" WHERE id={id}')
        connection.commit()
    elif option == 3:
        pokedex = input('type the new pokedex: ')
        id = int(input('type the id of the pokemon you want to edit: '))
        cursor.execute(f'UPDATE pokemons_list SET kind = "{pokedex}" WHERE id={id}')
        connection.commit()
    elif option == 4:
        level = input('type the new level: ')
        id = int(input('type the id of the pokemon you want to edit: '))
        cursor.execute(f'UPDATE pokemons_list SET kind = "{level}" WHERE id={id}')
        connection.commit()
    else:
        print('please choose a option between 1 and 4!')


def list_pokemons():
    cursor.execute('SELECT * FROM pokemons_list')
    for pokemon in cursor.fetchall():
        pokemons_list.append(pokemon[1])

    print(pokemons_list)


def delete():
    id = int(input('type the id of the pokemon you want to delete: '))
    cursor.execute(f'DELETE FROM pokemons_list WHERE id={id}')
    connection.commit()


cursor.execute('SELECT * FROM pokemons_list')
for pokemon in cursor.fetchall():
    print(f'{pokemon[0]} - {pokemon[1]} - {pokemon[2]} - {pokemon[3]} - {pokemon[4]}')


create()
buff_up()
edit()
delete()
list_pokemons()

cursor.close()
connection.close()
