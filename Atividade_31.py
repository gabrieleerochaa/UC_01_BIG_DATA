sexo = []
olhos = []
cabelos = []
idade = []
resp = "s"
qtd_sexo_idade = 0
qtd_olhos_cabelos = 0
while resp == "S" or resp == "s":
    sexo.append (input("Informe o sexo do individuo: "))
    olhos.append (input("Informe a cor dos olhos: "))
    cabelos.append (input("Informe a cor do cabelo: "))
    idade.append (int(input("Informe a idade: ")))
    resp = input("Deseja Continua(S/N)? ")
for i in range(len(sexo)):
    if (idade >= 18 and idade <= 35): qtd_sexo_idade += 1
    if qtd_olhos_cabelos += 1
print(f"A média das idades é {(sum(idade)/len(idade))} anos")
print(f"A maior idade é {max(idade)} anos")
print(f"A menor idade é {min(idade)} anos")
print(f"A quantidade de pessoas do sexo feminino com idades entre 18 e 35 anos é {qtd_sexo_idade}")
print(f"A quantidade de pessoas que possuem cabelos louros e olhos verdes é {qtd_olhos_cabelos}")