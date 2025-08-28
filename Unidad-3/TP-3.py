#Ejercicio 1
edad = int(input("Ingrese su edad"))
if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
#Ejercicio 2
nota = int(input("Ingrese su nota"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un numero"))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor ingrese un numero par")

#Ejercicio 4
edad = int(input("Ingrese su edad"))
if edad < 12:
    print("Usted pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categoria Adolecente")
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoria Adulto/a joven")
elif edad >= 30:
    print("Usted pertenece a la categoria Adulto/a")
    
#Ejercicio 5
contraseña = input("Ingrese su contraseña ")
cantidad_letras = len(contraseña)
if cantidad_letras >= 8 and cantidad_letras <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mode, median, mean 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

mi_media  = mean(numeros_aleatorios)
mi_mediana  = median(numeros_aleatorios)
mi_moda  = mode(numeros_aleatorios)

print("Mi media", mi_media)
print("Mi Mediana", mi_mediana)
print("Mi moda", mi_moda)

if mi_media > mi_mediana > mi_moda:
    print("La distribucion tiene sesgo positivo (hacia la derecha).")
elif mi_media < mi_mediana < mi_moda:
    print("La distribucion tiene sesgo negativo (hacia la izquierda).")
elif mi_media == mi_mediana == mi_moda:
    print("La distribucion no tiene sesgo")
else :
    print("No hay un sesgo claro segun estos criterios")

#Ejercicio 7
frase = input("Ingrese una frase ")
ultima_letra = frase[-1]
if ultima_letra == "a" and "e" and "i" and "o" and "u":
    print(frase,"!" )
else :
    print(frase)

#Ejercicio 8
nombre = input("Ingrese su nombre ")
numero = int(input("Seleccione un numero 1,2,3 "))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
else:
    print(nombre.title())

#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto "))
if magnitud < 3 :
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print(" Leve (ligeramente perceptible). ")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10
hemisferio = input("Ingrese en que hemsiferio se encuntra (N o S) ")
mes = int(input("Ingrese en que mes se encuentra "))
dia = int(input("Ingrese el dia "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Primavera")
else:
    print("Ingrese un Hemisferio Valido")
