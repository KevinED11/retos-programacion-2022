'''
* Escribe un programa que imprima los 50 primeros números de la sucesión
* de Fibonacci empezando en 0.
* - La serie Fibonacci se compone por una sucesión de números en
*   la que el siguiente siempre es la suma de los dos anteriores.
*   0, 1, 1, 2, 3, 5, 8, 13...
'''


def fibonacci(numbers):

    a, b = 0, 1

    fibonnaci_numbers = []

    for number in range(numbers):
        fibonnaci_numbers.append(a)

        a, b = b, a + b

    return fibonnaci_numbers


def fibonacci2(numbers):

    fibonacci_numbers = [0, 1]

    for i in range(2, numbers):

        fibonacci_numbers.append(
            fibonacci_numbers[i-1] + fibonacci_numbers[i-2])

    return fibonacci_numbers


if __name__ == '__main__':

    print(fibonacci(50))

    print('\n')

    print(fibonacci2(50))
