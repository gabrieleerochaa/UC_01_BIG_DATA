horas = int(input("Informe as horas trabalhadas ao mês: "))
valor = float(input("Informe o valor das horas trabalhadas: "))
bruto =  horas  * valor
inss = bruto * 0.08 
irrf = bruto * 0.11
sindicato = bruto * 0.05
liquido = bruto - (inss + irrf + sindicato)
print(f"O salário bruto é R$ {bruto:.2f}")
print(f"O desconto do inss é R$ {inss:.2f}")
print(f"O desconto do irrf é R$ {irrf:.2f}")
print(f"O desconto do sindicato é R$ {sindicato:.2f}")
print (f"O salário a receber é R$ {liquido:.2f} ")