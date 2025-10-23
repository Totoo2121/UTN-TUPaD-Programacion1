def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")
def sumar_digitos(num):
    if num < 10:
        return num
    else:
        return (num % 10) + sumar_digitos(num//10)


numero = pedir_entero("Ingrese un numero entero\n")
print(sumar_digitos(numero))
