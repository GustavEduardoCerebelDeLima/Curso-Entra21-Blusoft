# from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name, specie, habitat):
#         self.habitat = habitat
#         self.name = name
#         self.specie = specie
#
#     @abstractmethod
#     def ask_food(self):
#         return True
#
#     def eat(self):
#         print(f'{self.name} ate...')
#
#
# class Feline(Animal):
#     def __init__(self, name, specie, habitat, gills, ears):
#         super().__init__(name, specie, habitat)
#         self.ears = ears
#         self.gills = gills
#
#     def ask_food(self):
#         print('Miauuuuu')
#
#     @staticmethod
#     def born():
#         print('born')
#
#     @classmethod
#     def die(cls):
#         print('died')
#
#
# cat = Feline('Cairo', 'cat', 'forest', True, 2)
# cat.ask_food()


class Animals(ABC):
    def __init__(self, specie, genre, habitat, diet):
        self.specie = specie
        self.genre = genre
        self.habitat = habitat
        self.diet = diet

    @abstractmethod
    def breath(self):
        print('the animal breaths')

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

    def breath(self):
        print('the human breaths better')

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
human.eat('Aplle')
human.sleep()
human.to_think()
human.have_reason()
human.breath()


class Feline(Animals):
    def __init__(self, specie, genre, habitat, diet, claws, paws):
        super().__init__(specie, genre, habitat, diet)
        self.claws = claws
        self.paws = paws

    def breath(self):
        print('the feline breaths well')

    def scratch(self):
        print('the feline is scratching')

    def walk(self):
        print('the feline is walking')


lion = Feline('feline', 'mammal', 'Africa', 'carnivore', 20, 4)
lion.scratch()
lion.walk()
lion.breath()


class Fish(Animals):
    def __init__(self, specie, genre, habitat, diet, swim=True, gills=True):
        super().__init__(specie, genre, habitat, diet)
        self.swim = swim
        self.gills = gills

    def breath(self):
        print('the fish breaths under water')

    def to_swim(self):
        print('the fish is swimming')

    def breath_water(self):
        if self.gills:
            print('the fish can breath')
        else:
            print('the fish can not breath')


fish = Fish('shark', 'fish', 'water', 'carnivore')
fish.to_swim()
fish.breath_water()
fish.breath()
