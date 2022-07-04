R = int(input("type the number: "))
G = int(input("type the number: "))
B = int(input("type the number: "))

if R > 255 or R < 0 and G > 255 or G < 0 and B > 255 or B < 0:
    print("wrong")
else:
    print(f"{R:02X}{G:02X}{B:02X}")

# w3 schools format
# take a look on PyScript