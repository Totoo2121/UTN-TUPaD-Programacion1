def mostar_Productos():
    nombre = ""
    precio = 0
    cantidad = 0
    with open("productos.txt", "r") as archivo:
     for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(f"Productos: {partes[0]} | Precio: {partes[1]} | Cantidad: {partes[2]} ")
archivo = open("Productos.txt", "a")
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,300.0,15\n")
    archivo.write("Goma,80.0,50\n")
with open ("productos.txt" , "a") as archivo:
    archivo.write(input("Ingrese un producto "))
mostar_Productos()
diccionario = {}
Diccionario_de_productos = [diccionario]
print("Diccionario", diccionario)       # diccionario = {nombre:partes[0], precio:partes[1], cantidad:partes[2]}        
