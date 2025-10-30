#---------------------------------------------------------------------------------------#
def pedir_flotante(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return float(valor)
        except ValueError:
            print("Error: Debes ingresar un numero decimal.")
#---------------------------------------------------------------------------------------#
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("ERROR: Debe ingresar un numero.")
#---------------------------------------------------------------------------------------#
def menu():
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Salir")

    while True:
        try:
            opcion = int(input("Elegi una opción: "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Opcion invalida. Solo 1, 2 o 3.")
        except:
            print("Debes ingresar un numero.")
#---------------------------------------------------------------------------------------#  
def buscar_elemento(lista, valor):
    if valor in lista:
        return True
    else:
        return False
#---------------------------------------------------------------------------------------#  
def promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)