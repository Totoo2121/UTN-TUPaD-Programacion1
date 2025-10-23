def pedir_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("ERROR: El numero debe ser positivo.")
        except ValueError:
            print("ERROR: Debe ingresar un numero valido.")


def contar_digito(n, d):
    if n < 10:
        if n == d:
            return 1
        else:
            return 0
    else:
        ultimo = n % 10
        resto = n // 10
        if ultimo == d:
            return 1 + contar_digito(resto, d)
        else:
            return contar_digito(resto, d)

numero = pedir_entero_positivo("Ingrese un numero entero positivo: ")
digito = pedir_entero_positivo("Ingrese un digito para buscarlo dentro del numero: ")

print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el numero {numero}.")
