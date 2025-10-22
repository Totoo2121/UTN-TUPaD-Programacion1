def potencia_de_un_numero(base,pote):
    if pote == 0:
        return 1
    else:
        return base * potencia_de_un_numero(base,pote -1)
base = int(input("Ingrese la base de la potecia "))
pote = int(input("Ingrese la potencia "))
resultado = potencia_de_un_numero(base,pote)
print(resultado)

