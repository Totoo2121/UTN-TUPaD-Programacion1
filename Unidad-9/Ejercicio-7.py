def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")

def contar_bloques(bloque):
    if bloque == 1:
        return 1
    else:
        return bloque +  contar_bloques(bloque-1)
#main
bloque = pedir_entero("Ingrese la cantidad de bloques \n")
print(contar_bloques(bloque))