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