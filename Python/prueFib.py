def Fibonacci(N):
    #Calcula el termino N de la sucesión de Fibonacci 1, 1, 2, 3, 5, 8...
    if (N == 1):
        return 1
    elif (N == 2):
        return 1
    else:
        return (Fibonacci(N-2) + Fibonacci(N-1))

def Fibonacci2(N):
    Fibonacci_cache={}
    def Calculo(N):
        nonlocal Fibonacci_cache
        if N in Fibonacci_cache:
            return Fibonacci_cache[N]
        elif N == 1:
            return 1
        elif N == 2:
            return 1
        else:
            nuevo = (Calculo(N-2) + Calculo(N-1))
            Fibonacci_cache[N] = nuevo
        return nuevo
    return Calculo(N)

print (Fibonacci(50))
#for i in range (1,50):
#  print(Fibonacci(i))

#for j in range (1,50):
#   print(Fibonacci2(j))
