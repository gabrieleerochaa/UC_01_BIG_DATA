soma_m = 0
soma_f = 0
cont_m = 0
cont_f = 0
media = 0
for i in range(5):
    idade = int(input("Informe a idade:"))
    sexo = input("Informe M - para Masculino e F - para Feminino: ")
    if sexo == "m" or sexo == "M":
       soma_m = soma_m + idade
       cont_m += 1
    if sexo == "f" or sexo == "F":
       soma_f = soma_f + idade
       cont_f += 1
media_m = soma_m / cont_m
media_f = soma_f / cont_f
print(f"A soma das idades dos homens é {soma_m}")
print(f"A soma das idades das mulheres é {soma_f}")
print(f"A média das idades dos homens é {media_m}")
print(f"A média das idades das mulheres é {media_f}")




        