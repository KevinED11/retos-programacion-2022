"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """


def fizz_buzz():

    numbers = list(range(1, 101))
    for number in numbers:

        if number % 3 == 0 and number % 5 == 0:
            print('fizzbuzz')

        elif number % 3 == 0:
            print('fizz')

        elif number % 5 == 0:
            print('buzz')

        else:
            print(number)

if __name__ == '__main__':
    fizz_buzz()

    print("\n".join(["fizzbuzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i) for i in
                     range(1, 101)]))

