class Vehicle:
    def __init__(self, cor, door, brand, model, year):
        self.cor = cor
        self.door = door
        self.brand = brand
        self.model = model
        self.year = year


    def __repr__(self):
        return repr(f'{self.brand} - {self.model} - {self.cor} - {self.door} - {self.year}')


    def turnon(self):
        print(f'vrum vrum to {self.brand}')


    def turnoff(self):
        print(f'vrum is over to {self.brand}')


# v1 = Vehicle('blue', '4', 'bmw', 'x4', 2018)
# v2 = Vehicle('black', '4', 'audi', 'a4', 2005)
#
# print(v1.brand, v2.brand)
# v1.turnon()
# v2.turnoff()


vehicles = []
for _ in range(2):
    cor = input('type the color:')
    door = input('type the door:')
    brand = input('type the brand:')
    model = input('type the model:')
    year = input('type the year:')
    register = Vehicle(cor, door, brand, model, year)
    vehicles.append(register)

print(repr(vehicles))
