#Ejercicio 1
multiplos = list(range(4, 101, 4))
print(multiplos)
#Ejercicio 2
cosas = ["comida", "UTN","futbol", "Programacion","perro" ]
print("Penultimo elemnto positivo",cosas[3])
print("Penultimo elemnto negativo",cosas[-2])
#Ejercicio 3
listaVacia = []
listaVacia.append("Programacion")
listaVacia.append("UTN")
listaVacia.append("Mendoza")
print(listaVacia)
#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "Leon"
animales[-1] = "Oso"
print("Lista", animales)
#Ejercicio 5
print("Lo que sucede en ese codigo es que se crea la lista numeros con distintos valores. Lo que hace la funcion numeros.remove(max(numeros)) es eliminar el numero mas grande de la lista en este caso 22 y luego imprime la lista sin el 22")
#Ejercicio 6
numeros = list(range(10,30,5))
print(numeros[0], numeros[1])
#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"] 
autos[1] = "scirocco" 
autos[2] = "Golf" 
print(autos)
#Ejercicio8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)
#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
compras[2].append("Jugo")
compras[1][1] = "Tallarines"
compras[0].remove("pan")
print(compras)
#Ejercicio 10
lista_anidada = [15,True, [25.5,57.9, 30.6],False]
print(lista_anidada)