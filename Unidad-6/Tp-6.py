#Ejercicio 1
def hola_mundo():
    print("Hola Mundo")
hola_mundo()
#Ejercicio 2
def saludar_usario(nombre):
    print("Hola", nombre)
nom = input("Ingrese su nombre ")
saludar_usario(nom)
#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")
nombre = input("Ingrese su nombre ")
apellido= input("Ingrese su apellido ")
edad = input("Ingrese su edad ")
residencia = input("Ingrese su residencia ")
informacion_personal(nombre,apellido,edad, residencia)
#Ejercicio 4
def calcular_area_circulo(radio):
    area = 3.14 * radio**2
    print("El area del circulo es ", area)
def  calcular_perimetro_circulo(radio):
    perimetro = 2*3.14*radio
    print("El perimetro del circulo es ", perimetro)
radio = int(input("Ingrese el radio del circulo "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
#Ejercicio 5
def segundos_a_horas(segundos):
    horas = segundos/3600
    print(f"La cantidad de horas son {horas} horas")
segundos = int(input("Ingrese la cantidad de segundos "))
segundos_a_horas(segundos)
#Ejercicio 6
def tabla_Multiplicar(numero):
    for i in range(0,11):
        tabla = numero * i
        print(f"{numero} x {i} = {tabla}")
numero = int(input("Ingrese el numero para conocer su Tabla de Multiplicar "))
tabla_Multiplicar(numero)
#Ejercicio 7
def operaciones_basicas(a,b):
    suma = (a + b)
    resta  = (a - b)
    multiplicacion = (a * b)
    division = (a / b)
    print(f"El resultado de {a} + {b} = {suma}")
    print(f"El resultado de {a} - {b} = {resta}")
    print(f"El resultado de {a} * {b} = {multiplicacion}")
    print(f"El resultado de {a} / {b} = {division}")
a = int(input("Ingrese un valor para numero A ")) 
b = int(input("Ingrese un valor para numero B ")) 
operaciones_basicas(a,b)
#Ejercicio 8
def calcular_imc(peso, altura):
    IMC =round( peso / altura **2)
    print("El IMC es ", IMC)
peso = int(input("Ingrese su peso "))
altura = float(input("Ingrese su altura "))
calcular_imc(peso,altura)
#Ejercicio 9
def  celsius_a_fahrenheit(celsius):
    fahrenheit = round(celsius * 1.8 + 32)
    print("Fahrenheit", fahrenheit)
celsius = float(input("Ingrese la temperatura en Celsius "))
celsius_a_fahrenheit(celsius)
#Ejercicio 10
def calcular_promedio(a, b, c):
    suma = a + b + c
    promedio = round(suma / 3)
    print("El promedio es ",promedio)
a = int(input("Ingrese un numero "))
b = int(input("Ingrese un segundo numero "))
c = int(input("Ingrese un tercer numero "))
calcular_promedio(a,b,c)