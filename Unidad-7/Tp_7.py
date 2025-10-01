#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300
print(precios_frutas)
#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(precios_frutas)
#Ejercicio 3
Lista_Frutas = [precios_frutas.keys()]
print(Lista_Frutas)
#Ejercicio 4
contactos = {}
for i in range(0,5):
    nombre = input("Ingrese el nombre del contacto")
    numero = int(input("Ingrese el numero de telefono del contacto"))
    contactos[nombre] = numero
print(contactos)
#Ejercicio 5
frase = input("Ingrese una frase ")
palabras = frase.split()
palabras_Unicas = set(palabras)

Recuento = {}
for i in palabras:
    if i in Recuento:
        Recuento[i] += 1
    else:
        Recuento[i] =1
print("Lista con palabras unicas", palabras_Unicas)
print("Palabras repetidas", Recuento)
#Ejercicio 6 
Alumno = input("Ingrese el alumno")
Alumnos = {Alumno}
print(Alumnos)

