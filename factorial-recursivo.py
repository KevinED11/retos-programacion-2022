'''
* Escribe una función que calcule y retorne el factorial de un número dado
* de forma recursiva.
'''


def numero_factorial(num: int) -> int:

    if num == 0:
        return 1
    else:
        return num * numero_factorial(num - 1)


print(numero_factorial(5))
