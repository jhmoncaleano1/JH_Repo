#creando una funcion que nos retorna la serie de fibonacci desde 0 hasta el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b,a+b
#resultado llama la funcion fibonacci con el parametro 34
resultado = fibonacci(34)
print(f"los numeros de la serie son : {resultado}")
       
      