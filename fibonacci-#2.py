'''
* Escribe un programa que imprima los 50 primeros números de la sucesión
* de Fibonacci empezando en 0.
* - La serie Fibonacci se compone por una sucesión de números en
*   la que el siguiente siempre es la suma de los dos anteriores.
*   0, 1, 1, 2, 3, 5, 8, 13...
'''


def fibonacci(num):

    a, b = 0, 1

    fibonnaci_numbers = []

    for number in range(num + 1):
        fibonnaci_numbers.append(a)

        a, b = b, a + b

    return fibonnaci_numbers


print(fibonacci(10))
