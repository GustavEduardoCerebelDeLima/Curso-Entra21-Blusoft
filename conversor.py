"""
-----------------------------------------
          Selecione uma opção
-----------------------------------------
1 - Convert from Celsius to Kelvin
2 - Convert from Celsius to Fahrenheit
3 - Convert from Kelvin to Celsius
4 - Convert from Kelvin to Fahrenheit
5 - Convert from Fahrenheit to Celsius
6 - Convert from Fahrenheit to Kelvin
"""
print(30*"-")
text = " Selecione uma opção"
text = text.center(30)
print(text)
print(30*"-")
print("1 - Convert from Celsius to Kelvin")
print("2 - Convert from Celsius to Fahrenheit")
print("3 - Convert from Kelvin to Celsius")
print("4 - Convert from Kelvin to Fahrenheit")
print("5 - Convert from Fahrenheit to Celsius")
print("6 - Convert from Fahrenheit to Kelvin")


option = float(input("what is your option: "))
if option == 1:
    cel = float(input("right a number: "))
    print(f"The temperature in Kelvin is {cel + 273.15}")
if option == 2:
    cel = float(input("right a number: "))
    print(f"The temperature in Fahrenheit is {(cel * 9/5) + 32}")
if option == 3:
    kelvin = float(input("right a number: "))
    print(f"The temperature in celsius is {(kelvin - 32) * 5/9}")
if option == 4:
    kelvin = float(input("right a number: "))
    print(f"The temperature in Fahrenheit is {(kelvin - 273.15) * 9/5 + 32}")
if option == 5:
    Fahrenheit = float(input("right a number: "))
    print(f"The temperature in celsius is {(Fahrenheit - 32) * 5/9 }")
if option == 6:
    Fahrenheit = float(input("right a number: "))
    print(f"The temperature in kelvin is {(Fahrenheit - 32) * 5/9 + 273.15 }")

"""
if op == 1:
    total = float(input('Digite o valor em Celsius'))
    total2 = total + 273.15
if op == 2:
    total = float(input('Digite o valor em Celsius'))
    total2 = total * 1.8 + 32
if op == 3:
    total = float(input('Digite o valor em Kelvin'))
    total2 = total - 273.15
if op == 4:
    total = float(input('Digite o valor em Kelvin'))
    total2 = (total - 273.15) * 1.8 + 32
if op == 5:
    total = float(input('Digite o valor em Fahrenheit'))
    total2 = (total -32) * (5/9)
if op == 6:
    total = float(input('Digite o valor em Fahrenheit'))
    total2 = (total -32) * (5/9) + 273.15
print(total2)
"""