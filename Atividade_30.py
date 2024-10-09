dia = []
temperatura = []
resp = "s"
while resp == "S" or resp == "s":
    dia.append (input("Informe o dia da semana: "))
    temperatura.append(float(input("Informe a temperatura: ")))
    resp = input("Deseja Continua(S/N)? ")
print(f"A maior temperatura é {max(temperatura)}°C")
print(f"A menor temperatura é {min(temperatura)}°C")
print(f"A média das temperaturas é {sum(temperatura)/len(temperatura):.2f}°C")
temperatura.sort()
print(temperatura)