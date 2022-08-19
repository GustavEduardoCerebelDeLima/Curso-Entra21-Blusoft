# 0	Rio Grande do Sul
# 1	Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins
# 2	Amazonas, Pará, Roraima, Amapá, Acre e Rondônia
# 3	Ceará, Maranhão e Piauí
# 4	Paraíba, Pernambuco, Alagoas e Rio Grande do Norte
# 5	Bahia e Sergipe
# 6	Minas Gerais
# 7	Rio de Janeiro e Espírito Santo
# 8	São Paulo
# 9	Paraná e Santa Catarina

cpf = input("type the cpf: ")

if cpf[10] == '0':
    print("Rio Grande do Sul")
elif cpf[10] == '1':
    print("Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins")
elif cpf[10] == '2':
    print("Amazonas, Pará, Roraima, Amapá, Acre e Rondônia")
elif cpf[10] == '3':
    print("Ceará, Maranhão e Piauí")
elif cpf[10] == '4':
    print("Paraíba, Pernambuco, Alagoas e Rio Grande do Norte")
elif cpf[10] == "5":
    print("Bahia e Sergipe")
elif cpf[10] == "6":
    print("Minas Gerais")
elif cpf[10] == "7":
    print("Rio de Janeiro e Espírito Santo")
elif cpf[10] == "8":
    print("São Paulo")
else:
    print("Paraná e Santa Catarina")
