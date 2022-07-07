#======================================================EX1==============================================================
# class Ball:
#     def __init__(self, color, circumference, material):
#         self.color = color
#         self.circumference = circumference
#         self.material = material
#
#     def change_color(self, new_color):
#         if self.color:
#             self.color = new_color
#
#
#     def show_color(self):
#         if self.color:
#             print(f'{self.color} is the ball color')
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

#======================================================EX3==============================================================

class Rectangle:
    def __init__(self, base, hight):
        self.base = base
        self.hight = hight

    def change_sides(self, new_base, new_hight):
        self.base = new_base
        self.hight = new_hight

    def sides_values(self):
        print(f'{self.base} is the new base')
        print(f'{self.hight} is the new hight')

    def area(self):
        return self.base * self.hight

    def perimeter(self):
        return (self.base * 2) + (self.hight * 2)


rec = Rectangle(int(input('type the base size: ')), int(input('type the base size: ')))
rec.change_sides(10, 10)
rec.sides_values()
print(rec.area())
size_floors = 2
floor_quantity = rec.area() / size_floors
print(floor_quantity)


