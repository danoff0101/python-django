

# consumo eletricidade
kwh = float(input("digite a quantidade de kwh consumida: "))
tipo = (input("digite o tipo de intalaçaõ: "))

if ((tipo == "r"),(kwh <= 500)) :
    preco = float(0.40)
    valorfinal=float (kwh*preco)
    print (valorfinal)
else:
        preco = 0.65
        valorfinal=float (kwh*preco)
        print (valorfinal)
    