name = input("type the name: ")
n1 = int(input("type the grade1: "))
n2 = int(input("type the grade2: "))
n3 = int(input("type the grade3: "))
n4 = int(input("type the grade4: "))

mean = (n1 + n2 + n3 + n4) / (4)

if mean < 3:
    print(f"{name}, not today, FARO")
elif mean < 5:
    print(f"{name}turn back twice")
elif mean < 7:
    print(f"{name}, you are in exam")
elif mean > 9:
    print(f"{name}, you are aproved")
elif mean < 10:
    print(f"{name},accredited**")
elif mean == 10:
    print(f"{name}, super accredited")










