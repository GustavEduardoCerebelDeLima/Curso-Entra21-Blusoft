import random
# Conta 1
#
# for i in range(1, 4):
#     print("OPERATION - SUBTRACTION")
#     print(30*"=")
#     print(f"count{i}!\n")
#     n1, n2 = int(input("type the number: ")), int(input("type the other number: "))
#     print(f"{n1} - {n2} = {n1 - n2}")
#     print(30*"=")
#     print("Second count\n")
#

# conta 2
# n = int(input("type the number: "))
# print("Even numbers: ", end="")
# for i in range(n): # possible answer (n + 1)
#     i += 1
#     if i % 2 != 0:
#         print(i, end=" ")

# # conta 3
# women_list = []
# men_list = []
# n = 0
# print("DOUBLE!\n")
# for i in range(1, 4):
#     w = input(f"type the name of the women {1}: ")
#     women_list.append(w)
# print(women_list)
# print()
# for i in range(1, 4):
#     m = input("type the name of the men: ")
#     men_list.append(m)
# print(men_list)
# print()
# for i in range(3):
#     print(f"Double{n}: {women_list[i]} e {men_list[i]}")
#     n += 1

# conta 4
# print("MULTIPLICATION TABLE!")
#
# while True:
#     option = int(input("Do you want to see a table?: (1) yes (2) no: "))
#     if option == 1:
#         n = int(input("type the number: "))
#         for i in range(1, 11):
#             print(f"{n} x {i:2} = {n * i}\n")
#     elif option == 2:
#         break
#     else:
#         continue
#


# conta 5

# print("PRODUCT REGISTRATION!")
# quantity = int(input("How many products do tou want to register?: "))
# print(f"Answer: {quantity}\n")
# print(50 * "=")
# product_list, price_list = [], []
#
# for i in range(quantity):
#     product = input("type the product: ")
#     product_list.append(product)
#     price = float(input("type the price: "))
#     print()
#     price_list.append(price)
# print(40 * "=")
#
# for i in range(quantity):
#     print(f"\nproduct{i}: {product_list[i]} - Price: {price_list[i]}")

# count 7
from random import randint

arquivo = open('times ex.7.txt', 'r')
times = arquivo.read().splitlines()
continuar = "S"

while True:
    pontos = [0] * len(times)
    cont_casa = 0
    cont_visita = 0
    for i in times:
        for j in times:
            if i == j:
                cont_visita += 1
                continue
            placar_casa = randint(0, 6)
            placar_visita = randint(0, 6)
            print(f'{i} [{placar_casa}] x [{placar_visita}] {j}')
            if placar_casa > placar_visita:
                pontos[cont_casa] += 3
            elif placar_visita > placar_casa:
                pontos[cont_visita] += 3
            else:
                pontos[cont_casa] += 1
                pontos[cont_visita] += 1

            cont_visita += 1
        cont_visita = 0
        cont_casa += 1

    print(pontos)
    maior_pont = max(pontos)
    time_campeao = pontos.index(maior_pont)

    print(f"CAMPEAO 2022 {times[time_campeao]} com {maior_pont} pontos")
    ranking = []
    for i in range(len(times)):
        ranking.append(f'{pontos[i]} - {times[i]}')

    ranking.sort(reverse=True)

    print()
    for i in ranking:
        print(i)

    opcao = input('Deseja continuar? ').upper()

    if opcao == "S":
        continue
    else:
        break


# file = open("times ex.7.txt", "r")
# teams = file.read().splitlines()
# print(teams)