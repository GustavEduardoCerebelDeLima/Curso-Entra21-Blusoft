# Question 2
n = int(input("type the number you want: "))
nfac = 0
cont = 1
while cont >= 1:
    nfac += (n - cont) * n
    cont += 1
    if (n - cont) == 0 or n < 0:
        break
print(nfac)





