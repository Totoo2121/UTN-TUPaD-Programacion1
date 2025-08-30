#Ejercicio 1
for i in range (1,100 +1):
    print(i)
#Ejercicio 2
numero = input("Ingrese un numero entero ")
print("La cantidad de digitos son " , len(numero))
#Ejercicio 3
numero1 = int(input("Ingrese el primer numero "))
numero2 = int (input("Ingrese un segundo numero "))
suma = 0
if numero1 < numero2:
    for i in range(numero1 + 1, numero2):
        suma = suma + i
print("El resultado es ", suma)
#Ejercicio 4
suma = 0 
while True:
    num = int(input("Ingrese numeros para sumar (Con 0 termina el programa)") )
    if num == 0:
        break
    else:
        suma = suma + num
print("La suma es ", suma)
#Ejercicio 5
import random
intentos = 0
ganaste = False
numero_aleatorio = random.randint(1, 9)
while not ganaste:
    numero = int(input("Ingrese un numero ") )
    if numero == numero_aleatorio:
        ganaste = True
        print("Ganaste el juego")
        print(f"El numero era {numero} Tus intentos fueron  {intentos}")
    else:
        intentos = intentos + 1
#Ejercicio 6 
for i in range (100,-1,-2) :
    print(i)
#Ejercicio 7
suma = 0
numero = int(input("Ingrese hasta que numero quiere sumar")) 
if numero > 0 :
    for i in range (0 , numero + 1):
        suma = suma + i 
print("La suma es " , suma)
#Ejercicio 8
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(0 , 100):
    numero = int(input(f"Ingrese un numero para la posicion {i + 1} " ))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if numero > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
print("Numeros Pares", pares)
print("Numeros Impares", impares)
print("Numeros Positivos", positivos)
print("Numeros Negativos", negativos)
#Ejercicio 9
suma = 0
media = 0
for i in range(1 , 10 +1):
    numero = int(input(f"Ingrese un numero para la posicion {i} " ))
    suma = suma + i
media = suma / 10
print(suma)
print("La media es " , media)
#Ejercicio 10
numero = input("Ingrese un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)