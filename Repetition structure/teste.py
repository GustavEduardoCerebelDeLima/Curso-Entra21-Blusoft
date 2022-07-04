inicio = "S"
while inicio == "S":
    cpf = input("CPF: ")
    cpf.replace(".", "")
    cpf = int(list(cpf))