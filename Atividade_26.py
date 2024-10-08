nomes = []
medias = []
resp = "s"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do estudante: "))
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja Continua(S/N)? ")
print(nomes)
print(medias)
