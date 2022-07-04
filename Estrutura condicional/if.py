name = input("type the name: ")
n1 = int(input("type the grade1: "))
n2 = int(input("type the grade2: "))
n3 = int(input("type the grade3: "))
n4 = int(input("type the grade4: "))

mean = (n1 + n2 + n3 + n4) / (4)



""" 
precedence order: () , *
"""
if mean >= 7:
    print(f"{name}, you passed mate")
elif mean >= 5:
    print(f"{name}, study more, you are in exam")
else:
    print(f"{name}, you are a dumb")





