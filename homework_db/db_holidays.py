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

    def edit_company_table(self):
        option = int(input('what do you want to edit [1] name [2] nationality [3] initials:'))
        if option == 1:
            name = input('type the new name: ')
            id = int(input('type the id of the company you want to edit: '))
            cursor.execute(f'UPDATE Airline_Companies SET name = "{name}" WHERE company_id={id}')
            connection.commit()
        elif option == 2:
            nationality = input('type the new nationality: ')
            id = int(input('type the id of the company you want to edit: '))
            cursor.execute(f'UPDATE Airline_Companies SET nationality = "{nationality}" WHERE company_id={id}')
            connection.commit()
        elif option == 3:
            initials = input('type the new initials: ')
            id = int(input('type the id of the company you want to edit: '))
            cursor.execute(f'UPDATE Airline_Companies SET initials = "{initials}" WHERE company_id={id}')
            connection.commit()
        else:
            print('Please, choose a option between 1 and 3!')

    def delete_company(self):
        id = int(input('type the id of the company you want to delete: '))
        cursor.execute(f'DELETE FROM Airline_Companies WHERE company_id={id}')
        connection.commit()

    def show_company_table(self):
        cursor.execute('SELECT * FROM Airline_Companies')
        for i in cursor.fetchall():
            print(f'{i[0]} - Company:{i[1]} - Nationality:{i[2]} - Initials:{i[3]}')


companies = Companies()


# companies.create_table_companiy()
# companies.insert_company()
# companies.show_company_table()
# companies.edit_company_table()
# companies.delete_company()
# companies.show_company_table()


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

    def edit_aircraft_table(self):
        option = int(input('what do you want to edit [1] model [2] available_seats [3] luggage_limit:'))
        if option == 1:
            model = input('type the new model: ')
            id = int(input('type the id of the aircraft you want to edit: '))
            cursor.execute(f'UPDATE Aircraft SET model = "{model}" WHERE aircraft_id={id}')
            connection.commit()
        elif option == 2:
            available_seats = input('type the new available_seats: ')
            id = int(input('type the id of the aircraft you want to edit: '))
            cursor.execute(f'UPDATE Aircraft SET available_seats = "{available_seats}" WHERE aircraft_id={id}')
            connection.commit()
        elif option == 3:
            luggage_limit = input('type the new luggage_limit: ')
            id = int(input('type the id of the aircraft you want to edit: '))
            cursor.execute(f'UPDATE Aircraft SET luggage_limit = "{luggage_limit}" WHERE aircraft_id={id}')
            connection.commit()
        else:
            print('Please, choose a option between 1 and 3!')

    def delete_aircraft(self):
        id = int(input('type the id of the aircraft you want to delete: '))
        cursor.execute(f'DELETE FROM Aircraft WHERE aircraft_id={id}')
        connection.commit()

    def show_aircraft_table(self):
        cursor.execute('SELECT * FROM Aircraft')
        for i in cursor.fetchall():
            print(f'{i[0]} - Model:{i[1]} - Available seats:{i[2]} - Luggage limit:{i[3]}kg')


aircraft = Aircraft()


# aircraft.create_table_aircraft()
# aircraft.insert_aircraft()
# aircraft.show_aircraft_table()
# aircraft.edit_aircraft_table()
# aircraft.delete_aircraft()
# aircraft.show_aircraft_table()


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

    def edit_airport_table(self):
        option = int(input('what do you want to edit\n'
                           '[1] name [2] initials [3] city\n'
                           '[4] state [5] country [6] continent:'))
        if option == 1:
            name = input('type the new name: ')
            id = int(input('type the id of the airport you want to edit: '))
            cursor.execute(f'UPDATE Airport SET name = "{name}" WHERE airport_id={id}')
            connection.commit()
        elif option == 2:
            initials = input('type the new initials: ')
            id = int(input('type the id of the airport you want to edit: '))
            cursor.execute(f'UPDATE Airport SET initials = "{initials}" WHERE airport_id={id}')
            connection.commit()
        elif option == 3:
            city = input('type the new city: ')
            id = int(input('type the id of the airport you want to edit: '))
            cursor.execute(f'UPDATE Airport SET city = "{city}" WHERE airport_id={id}')
            connection.commit()
        elif option == 4:
            state = input('type the new state: ')
            id = int(input('type the id of the airport you want to edit: '))
            cursor.execute(f'UPDATE Airport SET state = "{state}" WHERE airport_id={id}')
            connection.commit()
        elif option == 5:
            country = input('type the new country: ')
            id = int(input('type the id of the airport you want to edit: '))
            cursor.execute(f'UPDATE Airport SET country = "{country}" WHERE airport_id={id}')
            connection.commit()
        elif option == 6:
            continent = input('type the new continent: ')
            id = int(input('type the id of the airport you want to edit: '))
            cursor.execute(f'UPDATE Airport SET continent = "{continent}" WHERE airport_id={id}')
            connection.commit()
        else:
            print('Please, choose a option between 1 and 6!')

    def delete_airport(self):
        id = int(input('type the id of the airport you want to delete: '))
        cursor.execute(f'DELETE FROM Airport WHERE airport_id={id}')
        connection.commit()

    def show_airport_able(self):
        cursor.execute('SELECT * FROM Airport')
        for i in cursor.fetchall():
            print(f'{i[0]} - Name:{i[1]} - Initials:{i[2]}'
                  f' - City:{i[3]} - State:{i[4]} - Country:{i[5]} - Continent:{i[6]}')


airport = Airport()


# airport.create_table_airport()
# airport.insert_airport()
# airport.show_airport_able()
# airport.edit_airport_table()
# airport.delete_airport()
# airport.show_airport_able()


class Fly:
    def __init__(self):
        pass

    def create_table_fly(self):
        cursor.execute('CREATE TABLE IF NOT EXISTS Fly('
                       'fly_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,'
                       'departure_date TEXT ,'
                       'departure_hour INTEGER ,'
                       'aircraft_id_taking_off INTEGER ,'
                       'aircraft_id_bound INTEGER ,'
                       'company_id INTEGER,'
                       'passengers INTEGER,'
                       'available_seats INTEGER,'
                       'carried_luggage INTEGER,'
                       'aircraft_id INTEGER,'
                       'arrival_date TEXT,'
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

    def edit_airport_table(self):
        option = int(input('what do you want to edit\n'
                           '[1] departure_date [2] departure_hour [3] aircraft_id_taking_off [4] aircraft_id_bound\n'
                           '[5] company_id [6] passengers [7] available_seats [8] carried_luggage\n'
                           '[9] aircraft_id [10] arrival_date [11] arrival_hour [12] fly_type:'))
        if option == 1:
            departure_date = input('type the new departure_date: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET departure_date = "{departure_date}" WHERE fly_id={id}')
            connection.commit()
        elif option == 2:
            departure_hour = input('type the new departure_hour: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET departure_hour = "{departure_hour}" WHERE fly_id={id}')
            connection.commit()
        elif option == 3:
            aircraft_id_taking_off = input('type the new aircraft_id_taking_off: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET aircraft_id_taking_off = "{aircraft_id_taking_off}" WHERE fly_id={id}')
            connection.commit()
        elif option == 4:
            aircraft_id_bound = input('type the new aircraft_id_bound: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET aircraft_id_bound = "{aircraft_id_bound}" WHERE fly_id={id}')
            connection.commit()
        elif option == 5:
            company_id = input('type the new company_id: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET company_id = "{company_id}" WHERE fly_id={id}')
            connection.commit()
        elif option == 6:
            passengers = input('type the new passengers: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET passengers = "{passengers}" WHERE fly_id={id}')
            connection.commit()
        elif option == 7:
            available_seats = input('type the new available_seats: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET available_seats = "{available_seats}" WHERE fly_id={id}')
            connection.commit()
        elif option == 8:
            carried_luggage = input('type the new carried_luggage: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET carried_luggage = "{carried_luggage}" WHERE fly_id={id}')
            connection.commit()
        elif option == 9:
            aircraft_id = input('type the new aircraft_id: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET aircraft_id = "{aircraft_id}" WHERE fly_id={id}')
            connection.commit()
        elif option == 10:
            arrival_date = input('type the new arrival_date: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET arrival_date = "{arrival_date}" WHERE fly_id={id}')
            connection.commit()
        elif option == 11:
            arrival_hour = input('type the new arrival_hour: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET arrival_hour = "{arrival_hour}" WHERE fly_id={id}')
            connection.commit()
        elif option == 12:
            fly_type = input('type the new fly_type: ')
            id = int(input('type the id of the fly you want to edit: '))
            cursor.execute(f'UPDATE Fly SET fly_type = "{fly_type}" WHERE fly_id={id}')
            connection.commit()
        else:
            print('Please, choose a option between 1 and 12!')

    def delete_fly(self):
        id = int(input('type the id of the fly you want to delete: '))
        cursor.execute(f'DELETE FROM Fly WHERE fly_id={id}')
        connection.commit()

    def fly_report(self):
        option = int(input('By which filter you want to see the results [1] Period [2] Company [3] Airport: '))
        if option == 1:
            departure_date = input('What the date of the departure you want to filter?:')
            try:            # using try to avoid the possible error if the value is not in the table
                cursor.execute(f'SELECT passengers,available_seats,carried_luggage FROM Fly'
                               f' WHERE departure_date="{departure_date}"')
                for i in cursor.fetchall():
                    print(f'Departure date {departure_date} - passengers:{i[0]}'
                          f' - available_seats:{i[1]} - carried_luggage:{i[2]}')
            except:
                print('Sorry, this date does not exists in our information! Try again!')
        elif option == 2:
            company_id = int(input('What the id of the company do you want to filter?: '))
            try:
                cursor.execute(f'SELECT passengers,available_seats,carried_luggage FROM Fly'
                               f' WHERE company_id={company_id}')
                for i in cursor.fetchall():
                    print(f'Company ID {company_id} - passengers:{i[0]} - available_seats:{i[1]} - carried_luggage:{i[2]}')
            except:
                print('Sorry, this id of the company does not exists in our information! Try again!')
        elif option == 3:
            aircraft_id_taking_off = int(input('What the id of the airport do you want to filter?: '))
            try:
                cursor.execute(f'SELECT passengers,available_seats,carried_luggage FROM Fly'
                               f' WHERE aircraft_id_taking_off={aircraft_id_taking_off}')
                for i in cursor.fetchall():
                    print(f'Airport ID {aircraft_id_taking_off} - passengers:{i[0]}'
                          f' - available_seats:{i[1]} - carried_luggage:{i[2]}')
            except:
                print('Sorry, this id of the airport does not exists in our information! Try again!')

    def show_fly_table(self):
        cursor.execute('SELECT * FROM Fly')
        for i in cursor.fetchall():
            print(f'{i[0]} - departure date:{i[1]} - departure hour:{i[2]} - aircraft id taking off:{i[3]}\n'
                  f'aircraft id bound:{i[4]} - company id:{i[5]} - passengers quantity:{i[6]} - available seats:{i[7]}\n'
                  f'carried luggage:{i[8]}kg - aircraft id:{i[9]} - arrival date:{i[10]}\n'
                  f'arrival hour:{i[11]} - fly type:{i[12]}')


fly = Fly()
# fly.create_table_fly()
# fly.insert_fly()
# fly.show_fly_table()
# fly.edit_airport_table()
# fly.delete_fly()
# fly.show_fly_table()
# fly.fly_report()

cursor.close()  # Always close because of attacks!
connection.close()
