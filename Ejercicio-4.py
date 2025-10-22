def binario(entero):
    if entero == 0:
        return ""
    else:
        cociente = entero // 2
        resto = entero % 2 
        return binario(cociente) + str(resto)
#main
entero = int(input("Ingrese un numero entero para conocer su binario"))
binario (entero)
print(binario(entero))
