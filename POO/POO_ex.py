class CocaCola:
    def __init__(self, hight, volume, diameter, material, lable):
        self.hight = hight
        self.volume = volume
        self.diameter = diameter
        self.material = material
        self.lable = lable

    def __repr__(self):
        return repr(f'{self.hight} - {self.volume} - {self.diameter} - {self.material} - {self.lable}')


    def open(self):
        print('the can is openned')


    def close(self):
        print('the can is closed')


    def drink(self):
        print('just drink dude')


    def drain_out(self):
        print('the can is empty')


    def crumple(self):
        print('the can is damaged')

    def take_lack_off(self):
        print('the can is nude')


    def throw_away(self):
        print('the can is gone')


can = []
for _ in range(1):
    height = input('type the height:')
    volume = input('type the volume:')
    diameter = input('type the diameter:')
    material = input('type the material:')
    lable = input('type the lable:')
    obj = CocaCola(height, volume, diameter, material, lable)
    can.append(obj)

print(repr(can))

