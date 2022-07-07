class CocaCola:
    def __init__(self, hight, volume, diameter, material= 'aluminium', lable='coke'): # '' is a default and it HAS to be in the end
        self.hight = hight
        self.volume = volume
        self.diameter = diameter
        self.material = material
        self.lable = lable
        self.lacre = True
        self.crumple = False
        self.throw_away = False
        self.openned = False


    def open(self):
        if self.openned:
            print('the can is already openned')
        else:
            print('the can was openned')
            self.openned = True


    def drink(self, quantity):
        if not self.openned:
            print('the can is closed!')
        elif quantity > self.volume:
            print(f'you drank {self.volume} and missing {quantity - self.volume} ')
            self.volume = 0
        else:
            self.volume -= quantity
            print(f'you drank {quantity} and in yhe can remains {self.volume}')


    def drain_out(self):
        if not self.openned:
            print('the can is closed, you can not drain it out!')
        else:
            print('can is empty')
            self.volume = 0


    def crumple(self):
        if not self.crumple and self.volume == 0:
            print('the can is crumpled')
            self.crumple = True
        else:
            print('you can not crumple')



    def take_lack(self):
        if self.lacre:
            self.lacre = False
            print('the lack was taken off')
        else:
            print('there is no lack')


    def throw_away(self):
        if self.crumple and not self.throw_away:
            print('throw away in the trash')
            self.throw_away = True
        else:
            print('first, crumple the can')


l1 = CocaCola(12, 5, 350)

l1.open()
l1.drink(5)
l1.drain_out()
l1.crumple()
l1.take_lack()
l1.throw_away()


# # Criar uma classe para uma lata de coca-cola.
# # A classe deve ter todos os atributos dimensionais,(Altura, diametro,volume)
# # e suas características de material()
# # As funcionalidades(métodos) da lata sao, abrir,
# # beber, esvaziar, amassar, retirar lacre, e descartar
#
# class Lata:
#     def __init__(self, altura, diametro, volume, material='aluminio', rotulo='coca'):
#         self.altura = altura
#         self.diametro = diametro
#         self.volume = volume
#         self.material = material
#         self.rotulo = rotulo
#         self.lacre = True
#         self.amassada = False
#         self.descartada = False
#         self.aberta = False
#
#     def abrir(self):
#         if self.aberta:
#             print('já está aberta, bocó')
#         else:
#             print('Lata foi aberta com sucesso')
#             self.aberta = True
#
#     def beber(self, quantidade):
#         if not self.aberta:
#             print('Lata ainda está fechada')
#         elif quantidade > self.volume:
#             print(f'Você bebeu {self.volume}, e ainda faltou {quantidade-self.volume}')
#             self.volume = 0
#         else:
#             self.volume -= quantidade
#             print(f'Você bebeu {quantidade}, e na lata ainda resta {self.volume}')
#
#     def esvaziar(self):
#         if not self.aberta:
#             print('Não dá pra esvaziar com a lata fechada')
#         else:
#             print('Lata vazia')
#             self.volume = 0
#
#     def amassar(self):
#         if not self.amassada and self.volume == 0:
#             print('Lata amassada')
#             self.amassada = True
#         else:
#             print('Não dá pra amassar')
#
#     def retirar_lacre(self):
#         if self.lacre:
#             self.lacre = False
#             print('Lacre retirado')
#         else:
#             print('Não tinha lacre')
#
#     def descartar(self):
#         if self.descartada:
#             print('Não pode descartar o que já está descartado')
#         elif self.amassada:
#             print('Descartada no lixeiro amarelo')
#             self.descartada = True
#         else:
#             print('Primeiro, amasse a lata')
#
#
# l1 = Lata(12.22, 5.2, 350)
# l1.abrir()
# l1.beber(300)
# l1.descartar()
# l1.esvaziar()
# l1.amassar()
# l1.retirar_lacre()
# l1.amassar()
# l1.descartar()
#







