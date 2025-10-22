def fibonacci(n):
    if n < 2:
        return n
    else:
        return  fibonacci(n-1) + fibonacci(n-2)

    
    
    
numero = int(input("Ingrese un numero para conocer Fibonacci "))
fibonacci(numero)
for i in range(numero):
        print(fibonacci(i))