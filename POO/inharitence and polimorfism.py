# class Vehicle:
#     def __init__(self, color, places, wheel_quantity, motor_type, value, year, brand, model):
#         self.color = color
#         self.places = places
#         self.wheel_quantity = wheel_quantity
#         self.motor_type = motor_type
#         self.value = value
#         self.year = year
#         self.brand = brand
#         self.model = model
#
#     def speed_up(self):
#         print('Speed up')
#
#     def break_up(self):
#         print('breaked up')
#
#     def turn_on(self):
#         print('turned on')
#
#     def turn_off(self):
#         print('turned off')
#
#
# class Bike(Vehicle):
#     def __init__(self, color, places, wheel_quantity, motor_type, value, year, brand, model, cram=False):
#         super().__init__(color, places, wheel_quantity, motor_type, value, year, brand, model)
#         self.cram = cram
#
#     def cam_up(self):
#         if self.cram:
#             print('it is cramed')
#         else:
#             print('crammmmm')
#             self.cram = True
#
#     def discram(self):
#         self.cram = False
#
#
# # b1 = Bike('blue', 2, 2, '125cc', 17000, 2022, 'Honda', 'cg-125', True)
# # b1.cam_up()
# # b1.discram()
# # b1.cam_up()
# # v1 = Vehicle('silver', 4, 4, '180 cv', 45000, 2012, 'Chevrolet', 'celta')
#
#
# class Car(Vehicle):
#     def __init__(self, color, places, wheel_quantity, motor_type, value, year, brand, model, doors, windows):
#         super().__init__(color, places, wheel_quantity, motor_type, value, year, brand, model)
#         self.doors = doors
#         self.window = windows
#
#     def open_door(self, quantity_door):
#         print(f'You opened {quantity_door} doors in your vehicle')
#
#     def open_windows(self, quantity_windows):
#         print(f'you opened {quantity_windows} windows\n')
#
#
# class Bus(Car):
#     def __init__(self, color, places, wheel_quantity, motor_type, value, year, brand, model, doors, windows, stairs, ticket_gate):
#         super().__init__(color, places, wheel_quantity, motor_type, value, year, brand, model, doors, windows)
#         self.stairs = stairs
#         self.ticket_gate = ticket_gate
#
#     def walk_stairs(self):
#         print('you are walking on the stairs to get on the bus')
#
#     def get_through(self):
#         print('you got through the ticket gate')
#
#
# car = Car('silver', 4, 4, '180 cv', 45000, 2012, 'Chevrolet', 'celta', 4, 4)
# car.open_door(4)
# car.open_windows(4)
#
# bus = Bus('gray', 4, 4, '100 cv', 10000, 2012, 'Mercedes', 'school', 4, 4, 'safe', 'pass')
# bus.open_door(4)
# bus.open_windows(4)
# bus.walk_stairs()
# bus.get_through()


class Animals:
    def __init__(self, specie, genre, habitat, diet):
        self.specie = specie
        self.genre = genre
        self.habitat = habitat
        self.diet = diet

    def eat(self, food):
        print(f'the animal eat {food}')

    def sleep(self):
        print('the animal is sleeping ')

    def die(self):
        print('the animal is dead')

    def poop(self):
        print('the animal is pooping')


class Human(Animals):
    def __init__(self, specie, genre, habitat, diet, think=True, reason=True):
        super().__init__(specie, genre, habitat, diet)
        self.reason = reason
        self.think = think

    def to_think(self):
        if self.think:
            print('the human thinks')
        else:
            print('the human is dead')

    def have_reason(self):
        if self.reason:
            print('the human has reason')
        else:
            print('he is dead or unconscious')


human = Human('human', 'mammal', 'earth', 'omnivorous', True, True)
human.die()
human.poop()
human.eat('aplle')
human.sleep()
human.to_think()
human.have_reason()


class Feline(Animals):
    def __init__(self, specie, genre, habitat, diet, claws, paws):
        super().__init__(specie, genre, habitat, diet)
        self.claws = claws
        self.paws = paws

    def scratch(self):
        print('the feline is scratching')

    def walk(self):
        print('the feline is walking')


lion = Feline('feline', 'mammal', 'Africa', 'carnivore', 20, 4)
lion.scratch()
lion.walk()

class Fish(Animals):
    def __init__(self, specie, genre, habitat, diet, swim=True, gills=True):
        super().__init__(specie, genre, habitat, diet)
        self.swim = swim
        self.gills = gills

    def to_swim(self):
        print('the fish is swimming')

    def breath(self):
        if self.gills:
            print('the fish can breath')
        else:
            print('the fish can not breath')


fish = Fish('shark', 'fish', 'water', 'carnivore')
fish.to_swim()
fish.breath()
