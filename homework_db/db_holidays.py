import sqlite3

connection = sqlite3.connect('Homework_Airlines_db.db')
cursor = connection.cursor()
print('connection successfully\n')


class Companies:
    def __init__(self):
        pass

    def create_table_companiy(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS Airline_Companies('
                       'company_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                       'name TEXT ,'
                       'nationality TEXT ,'
                       'initials TEXT)')

        connection.commit()

    def insert_company(self):
        name = input('type the name: ')
        nationality = input('type the nationality: ')
        initials = input('type the initials: ')
        cursor.execute('INSERT INTO Airline_Companies('
                       'name, nationality, initials)'
                       'VALUES (?, ?, ?)', (name, nationality, initials))

        connection.commit()

    def show_table(self):
        cursor.execute('SELECT * FROM Airline_Companies')
        for i in cursor.fetchall():
            print(f'{i[0]} - Company:{i[1]} - Nationality:{i[2]} - Initials:{i[3]}')


companies = Companies()


# companies.create_table_companiy()
# companies.insert_company()
# companies.show_table()


class Aircraft:
    def __init__(self):
        pass

    def create_table_aircraft(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS Aircraft('
                       'aircraft_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                       'model TEXT ,'
                       'available_seats INTEGER ,'
                       'luggage_limit INTEGER)')

        connection.commit()

    def insert_aircraft(self):
        model = input('type the model: ')
        available_seats = int(input('type the available_seats: '))
        luggage_limit = int(input('type the luggage_limit: '))
        cursor.execute('INSERT INTO Aircraft('
                       'model, available_seats, luggage_limit)'
                       'VALUES (?, ?, ?)', (model, available_seats, luggage_limit))

        connection.commit()

    def show_table(self):
        cursor.execute('SELECT * FROM Aircraft')
        for i in cursor.fetchall():
            print(f'{i[0]} - Model:{i[1]} - Available seats:{i[2]} - Luggage limit:{i[3]}kg')


aircraft = Aircraft()


# aircraft.create_table_aircraft()
# aircraft.insert_aircraft()
# aircraft.show_table()


class Airport:
    def __init__(self):
        pass

    def create_table_airport(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS Airport('
                       'airport_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                       'name TEXT ,'
                       'initials TEXT ,'
                       'city TEXT ,'
                       'state TEXT ,'
                       'country TEXT,'
                       'continent TEXT)')

        connection.commit()

    def insert_airport(self):
        name = input('type the name: ')
        initials = input('type the initials: ')
        city = input('type the city: ')
        state = input('type the state: ')
        country = input('type the country: ')
        continent = input('type the continent: ')
        cursor.execute('INSERT INTO Airport('
                       'name, initials, city, state, country, continent)'
                       'VALUES (?, ?, ?, ?, ?, ?)', (name, initials, city, state, country, continent))

        connection.commit()

    def show_table(self):
        cursor.execute('SELECT * FROM Airport')
        for i in cursor.fetchall():
            print(f'{i[0]} - Name:{i[1]} - Initials:{i[2]}'
                  f' - City:{i[3]} - State:{i[4]} - Country:{i[5]} - Continent:{i[6]}')


airport = Airport()


# airport.create_table_airport()
# airport.insert_airport()
# airport.show_table()


class Fly:
    def __init__(self):
        pass

    def create_table_fly(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS Fly('
                       'fly_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                       'departure_date TEXT ,'
                       'departure_hour TEXT ,'
                       'aircraft_id_taking_off INTEGER ,'
                       'aircraft_id_bound INTEGER ,'
                       'company_id INTEGER,'
                       'passengers INTEGER,'
                       'available_seats INTEGER,'
                       'carried_luggage INTEGER,'
                       'aircraft_id INTEGER,'
                       'arrival_date INTEGER,'
                       'arrival_hour INTEGER,'
                       'fly_type TEXT)')

        connection.commit()

    def insert_fly(self):
        departure_date = input('type the departure_date: ')
        departure_hour = input('type the departure_hour: ')
        aircraft_id_taking_off = input('type the aircraft_id_taking_off: ')
        aircraft_id_bound = input('type the aircraft_id_bound: ')
        company_id = input('type the company_id: ')
        passengers = input('type the passengers: ')
        available_seats = input('type the available_seats: ')
        carried_luggage = input('type the carried_luggage: ')
        aircraft_id = input('type the aircraft_id: ')
        arrival_date = input('type the arrival_date: ')
        arrival_hour = input('type the arrival_hour: ')
        fly_type = input('type the fly_type: ')
        cursor.execute('INSERT INTO Fly('
                       'departure_date, departure_hour,'
                       ' aircraft_id_taking_off, aircraft_id_bound,'
                       'company_id, passengers, available_seats, carried_luggage,'
                       'aircraft_id, arrival_date, arrival_hour, fly_type)'
                       'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (departure_date, departure_hour,
                                                                       aircraft_id_taking_off, aircraft_id_bound,
                                                                       company_id, passengers, available_seats,
                                                                       carried_luggage,
                                                                       aircraft_id, arrival_date, arrival_hour,
                                                                       fly_type))

        connection.commit()

    def show_table(self):
        cursor.execute('SELECT * FROM Fly')
        for i in cursor.fetchall():
            print(f'{i[0]} - departure date:{i[1]} - departure hour:{i[2]} - aircraft id taking off:{i[3]}\n'
                  f' - aircraft id bound:{i[4]} - company id:{i[5]} - passengers:{i[6]} - available seats:{i[7]}\n'
                  f' - carried luggage:{i[8]}kg - aircraft id:{i[9]} - arrival date:{i[10]}\n'
                  f' - arrival hour:{i[11]} - fly type:{i[12]}')


fly = Fly()
# fly.create_table_fly()
# fly.insert_fly()
# fly.show_table()


cursor.close()
connection.close()
