def fibonacci(n, depth=0):
    print(" " * depth + f"fibonacci({n})")
    if n <= 1:
        return n
    else:
        return fibonacci(n-1, depth+1) + fibonacci(n-2, depth+1)

# Ejemplo de uso
n = 5
print(f"Fibonacci de {n} es {fibonacci(n)}")