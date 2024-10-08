# Prestacao em atraso
prestacao =  float(input("Informe o valor da prestacao: "))
taxa = float(input("Informe a taxa de juros mensal: "))
tempo = int(input("Informe a quantidade de meses em atraso: "))
valor_final = prestacao+(prestacao*taxa/100*tempo)
print(f"o valor em atraso será de R${valor_final:.2f}")
