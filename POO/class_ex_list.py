#======================================================EX1==============================================================
# class Ball:
#     def __init__(self, color, circumference, material):
#         self.color = color
#         self.circumference = circumference
#         self.material = material
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
#     def show_color(self):
#         print(f'{self.color} is the ball color')
#
#
# b1 = Ball('blue', 20, 'leather')
# print(b1.color)
# b1.change_color(input('type the new color:'))
# b1.show_color()

#======================================================EX2==============================================================

# class Square:
#     def __init__(self, side_size):
#         self.side_size = side_size
#
#     def change_side(self, new_side):
#         self.side_size = new_side
#         print(f'{self.side_size} is the new size')
#
#     def side_value(self):
#         print(f'{self.side_size} is the size of the square')
#
#     def area(self):
#         area = self.side_size**2
#         print(f'the area is {area}')
#
#
# s1 = Square(4)
# s1.change_side(7)
# s1.area()

# #======================================================EX3==============================================================

# class Rectangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def change_sides(self, new_base, new_height):
#         self.base = new_base
#         self.height = new_height
#
#
#     def sides_values(self):
#         print(f'{self.base} is the new base')
#         print(f'{self.height} is the new height')
#
#     def area(self):
#         return self.base * self.height
#
#     def perimeter(self):
#         return (self.base * 2) + (self.height * 2)
#
#
# rec = Rectangle(int(input('type the base size: ')), int(input('type the base size: ')))
# rec.change_sides(10, 10)
# rec.sides_values()
# print(rec.area())
# size_floors = 2
# floor_quantity = rec.area() / size_floors
# print(floor_quantity)

# ==================================================EX4=================================================================

# class FuelPump:
#     def __init__(self, type_fuel, liter_value, fuel_quantity):
#         self.type_fuel = type_fuel
#         self.liter_value = liter_value
#         self.fuel_quantity = fuel_quantity
#
#     def to_fuel_value(self, put):
#         print(f'you want to fuel {put} dollars')
#         print(f'you got {put/self.liter_value:.2f} liters fueled')
#         self.fuel_quantity -= (put/self.liter_value)
#
#     def to_fuel_liter(self, put_quantity):
#         fuel_value = self.liter_value * put_quantity
#         print(f'\nyou have put {put_quantity} liters and it cost {fuel_value} for you')
#         self.fuel_quantity -= put_quantity
#
#     def change_value(self, new_value):
#         self.liter_value = new_value
#         print(f'\nnow thw value of the liter is {self.liter_value:.2f}')
#
#     def change_fuel(self, new_fuel):
#         self.type_fuel = new_fuel
#         print(f'\nthe fuel is now {self.type_fuel}')
#
#     def change_quantity(self, new_quantity):
#         self.fuel_quantity = new_quantity
#         print(f'\nnow we got {self.fuel_quantity:.2f} liters in the pump')
#
#
# b1 = FuelPump(input('type of fuel: '), int(input('value of fuel: ')), int(input('fuel quantity: ')))
# b1.to_fuel_value(50)
# b1.to_fuel_liter(5)
# print(f' we got {b1.fuel_quantity} litres in the pump after this fueling')
# b1.change_value(10)
# b1.change_fuel("oil")
# b1.change_quantity(50)
# b1.to_fuel_value(10)
# b1.to_fuel_liter(10)
# print(f' we got {b1.fuel_quantity} litres in the pump after this fueling')

# ==================================================EX5=================================================================

# class Monkey:
#     def __init__(self, name, stomach='nothing here'):
#         self.name = name
#         self.stomach = stomach
#         self.active = True
#
#     def eat(self, food):
#         if self.active:
#             self.stomach = food
#         else:
#             print('this monkey does not exist')
#
#     def see_stomach(self):
#         if self.active:
#             print(f'the monkey {self.name} ate {self.stomach} and he is done')
#         else:
#             print('this monkey does not exist')
#
#     def digest(self, digest_phase):
#         if self.active:
#             print(f'the monkey {self.name} ate {self.stomach} and he is at {digest_phase} digestion phase')
#         else:
#             print('this monkey does not exist')
#
#         if digest_phase == 'finished':
#             print(f'now {self.name} can eat again!')
#         else:
#             print(f'{self.name} you have to wait for your digestion finish to eat again!')
#
#     def delete_monkey(self):
#         if self.eat(input('type the name of the other monkey: ')):
#             self.active = False
#
#
# while True:
#     m1 = Monkey(input('type the name of the monkey: '))
#     m2 = Monkey(input('type the name of the other monkey: '))
#     m1.eat(input('type the food to the monkey: '))
#     m2.eat(input('type the food to the monkey: '))
#     m1.see_stomach()
#     m2.see_stomach()
#     m1.digest(input('tpy the phase of digestion:'))
#     m2.digest(input('tpy the phase of digestion:'))
#     m1.eat(m2.name)
#     m1.digest('finished')
#     m2.see_stomach()
#     option = input('do you want to continue? [1] S [2] N : ').upper()
#     if option == 'S':
#         continue
#     else:
#         break

# ==================================================EX6=================================================================

# class Tamagotchi:
#     def __init__(self, name, hungry, health, age):
#         self.name = name
#         self.hungry = hungry
#         self.health = health
#         self.age = age
#
#     def alter(self, new_name, new_hungry, new_health, new_age):
#         self.name = new_name
#         self.hungry = new_hungry
#         self.health = new_health
#         self.age = new_age
#
#     def show(self):
#         print(f'new name: {self.name} is now {self.hungry}% hungry, {self.health}% health and, nowadays, is {self.age} years old')
#
#     def mood(self):
#         if (self.hungry < 0 or self.hungry > 100) or (self.health < 0 or self.health > 100):
#             print('adjust the hungry and health values')
#         elif (0 < self.hungry < 25) and (0 < self.health < 25):
#             print(f'{self.name} is with bad mood today')
#         elif (25 < self.hungry < 50) and (25 < self.health < 50):
#             print(f'{self.name} is with normal mood today')
#         elif self.hungry > 50 and self.health > 50:
#             print(f'{self.name} is with good mood today')
#
#
# while True:
#     tamagotchi = Tamagotchi(input('name:'), int(input('hungry:')), int(input('health:')), int(input('age: ')))
#     print(f'{tamagotchi.name} is {tamagotchi.hungry}% hungry, {tamagotchi.health}% health and he is {tamagotchi.age}')
#     tamagotchi.alter(input(' new name:'), int(input('new hungry:')), int(input('new health:')), int(input('new age: ')))
#     tamagotchi.show()
#     tamagotchi.mood()
#
#     option = input('do you want to continue? [1] S [2] N : ').upper()
#     if option == 'S':
#         continue
#     else:
#         break

# ==================================================EX7=================================================================

# class TeleVision:
#     def __init__(self, height, length, width, color):
#         self.height = height
#         self.length = length
#         self.width = width
#         self.color = color
#         self.on = False
#
#     def turn_on(self):
#         self.on = True
#
#     def channel(self):
#         if not self.on:
#             print(f'you can not change channel without turning on the TV!')
#         else:
#             channels_num = 20
#             print(f'you have {channels_num} channels in your tv')
#
#     def change_channel(self, channels):
#         pass
#
#
# tv = TeleVision(10, 10, 10, 'black')
# tv.turn_on()
# tv.channel()

# ==================================================EX8=================================================================

# class Car:
#     def __init__(self, consume, max_tank=50):
#         self.__consume = consume
#         self.__max_tank = max_tank
#         self.__fuel_quantity = 0
#
#     def add_gas(self, liters):
#         self.__fuel_quantity += liters
#
#     def verify_fuel(self):
#         print(f'you got {self.__fuel_quantity} liters')
#
#     def ride(self, distance):
#         liter = distance / self.__consume
#         if liter > self.__consume:
#             print(f'there is no gas enough')
#         else:
#             self.__fuel_quantity -= liter
#             print(f'the trip was hit!')
#
#
# ferrari = Car(15)
# ferrari.add_gas(50)
# ferrari.ride(100)
# ferrari.verify_fuel()
