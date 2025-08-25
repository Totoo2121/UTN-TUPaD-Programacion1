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