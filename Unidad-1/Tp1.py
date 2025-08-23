
#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
edad = input ("Ingrese su edad")
residencia = input("Ingrese su pais de residencia")
bienvenida = (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")
print (bienvenida)

#Ejercicio 4
radio = int (input("Ingrese el radio del circulo "))
area = 3.14 * ( radio**2) 
circunferencia = 2 * 3.14 * radio
print("EL area es",area )
print(f"La circunferencia  es {circunferencia}" )

#Ejercicio 5
segundos = int (input("Ingrese una cantidad de segundos"))
hora = segundos / 3600
print (f"Los segundos equivalen a {hora}")

#Ejercicio 6
num = int(input("Ingrese el número para ver su tabla de multiplicar: "))

r1 = num * 1
r2 = num * 2
r3 = num * 3
r4 = num * 4
r5 = num * 5
r6 = num * 6
r7 = num * 7
r8 = num * 8
r9 = num * 9
r10 = num * 10

print(f"{num} x 1 = {r1}")
print(f"{num} x 2 = {r2}")
print(f"{num} x 3 = {r3}")
print(f"{num} x 4 = {r4}")
print(f"{num} x 5 = {r5}")
print(f"{num} x 6 = {r6}")
print(f"{num} x 7 = {r7}")
print(f"{num} x 8 = {r8}")
print(f"{num} x 9 = {r9}")
print(f"{num} x 10 = {r10}")

#Ejercicio 7
numero1 = int(input("Ingrese el valor de numero 1 (mayor a 0)"))
numero2 = int(input("Ingrese el valor de numero 2 (mayor a 0)"))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print("Resultado Suma " , suma)
print("Resultado Resta " , resta)
print("Resultado Multiplicacion " , multiplicacion)
print("Resultado Division " , division)

#Ejercicio 8
altura = float(input("Ingrese su altura"))
peso = float(input("Ingrese su peso"))
IMC = peso / altura **2
print("Su Indice de Masa Corporal es de ", IMC)

#Ejercicio 9
temperatura = float(input("Ingrese la temperatura en grados Celsius"))
Fahrenheit = 9/5 * temperatura + 32
print("Temperatura en Fahrenheit es" , Fahrenheit)

#Ejercicio 10
num1 = int(input ("Ingrese el valor del primer numero"))
num2 = int(input ("Ingrese el valor del segundo numero"))
num3 = int(input ("Ingrese el valor del tercer numero"))
promedio = (num1 + num2 + num3) / 3
print("El promedio es " , promedio)