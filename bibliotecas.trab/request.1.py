# ex 1

# import bibliotecas.trab
#
# letter = input('type the letter you want: ').upper()
# req = bibliotecas.trab.get('https://api-s-38ea2-default-rtdb.firebaseio.com/Escolas.json')
# schools = req.json()
#
# for i in schools:
#     if i[0] == letter:
#         print(i, schools[i])


#==========================================================EX2==========================================================


# req = bibliotecas.trab.get('https://api-s-38ea2-default-rtdb.firebaseio.com/Escolas.json')
# schools = req.json()
#
# for i in schools:
#     if len(i) >= 8 and len(i) <= 14:
#         print(f'{i}: is a big name')
#     elif len(i) > 14:
#         print(f'{i}: is a very big name')
#     elif len(i) < 8:
#         print(f'{i}: is a small name')

#==========================================================EX3==========================================================

# teams = bibliotecas.trab.get('https://times-5e780-default-rtdb.firebaseio.com/Times.json')
# info = '{"Cairo": "Flamengo"}'
# firebase = bibliotecas.trab.post('https://times-5e780-default-rtdb.firebaseio.com/Times.json', data=info)
# print(teams.json())

#==========================================================EX4==========================================================

# colors = bibliotecas.trab.get('https://cores-d86c6-default-rtdb.firebaseio.com/Cores/.json')
# # print(colors.json())
#
# cor1 = int(input('choose your color (1) Azul, (2) Amarelo, (4) Vermelho: '))
# cor2 = int(input('choose your color (1) Azul, (2) Amarelo, (4) Vermelho: '))
#
# if cor1 == cor2:
#     cor = cor1
# else:
#     cor = cor1 + cor2
#
# print(colors.json()[cor])

#=======================================================================================================================

# test
# 5
# CEP = input('insira seu cep: ')
# req = bibliotecas.trab.get(f'http://viacep.com.br/ws/{CEP}/json/')
#
# for i in req.json():
#     print(req.json()[i])
# 89012170


# 4
# CEP = bibliotecas.trab.get('https://cep.awesomeapi.com.br/json/05424020')

# for i in CEP.json():
#     print(f'{i}: {CEP.json()[i]}')
