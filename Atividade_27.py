nomes = []
medias = []
resp = "s"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do estudante: "))
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja Continua(S/N)? ")
for i in range(len(medias)):
    maior_media = max(medias)
    pos = medias.index(maior_media)
print(f"{nomes[pos]}, você possui a maior média")
print(f"A media da turma é {(sum(medias)/len(medias))}")
print(f"A maior média da turma é {max(medias)}")
print(f"A menor média da turma é {min(medias)}")
print(f"A amplitude da media da turma é {max(medias)- min(medias)}")
medias.sort()
print(medias)
