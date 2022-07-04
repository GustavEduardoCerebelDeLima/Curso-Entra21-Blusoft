contador = 2
numero = int(input('Digite um número: '))

if numero == 1:
    print('Não é primo')
else:
    while contador < numero:
        if numero % contador == 0:
            print("Não é primo")
            break
        contador += 1
    if contador == numero or numero == 2:
        print('É primo')



