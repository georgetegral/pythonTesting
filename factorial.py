def factorial(n):
    """
    Obtiene la factorial de un número de manera recursiva
    """
    if (n == 1):
        return 1
    
    return n * factorial(n-1)

numero = int(input('Escribe un entero: '))

print(f'{numero}! = {factorial(numero)}')