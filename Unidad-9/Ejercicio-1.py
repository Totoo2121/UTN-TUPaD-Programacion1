def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
numero = int(input("Ingrese un numero para conocer el factorial"))
print(factorial(numero))