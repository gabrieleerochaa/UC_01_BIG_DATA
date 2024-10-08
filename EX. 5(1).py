import datetime
data_atual= datetime.date.today
nome = input("Informe o seu Nome: ")
ano_nasc = int(input("Informe o Ano de Nascimento"))
idade = data_atual.year - ano_nasc
print("Sr(ª)", nome, "a sua idade é "idade", anos")
