try: 
    n1 = int(input("Forneça um valor inteiro"))
    n2 = int(input("Forneça outro valor inteiro"))
except ValueError:
    print("Verifique a entrada de dados")
else:
     try:
        result = n1 / n2
     except ZeroDivisionError:
        print("Não é possivel dividir por Zero")
     else:
      print (result)

 