'''
* Reto  # 3
* ¿ES UN NÚMERO PRIMO?

* Dificultad: MEDIA
*
* Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
* Hecho esto, imprime los números primos entre 1 y 100.
'''


def es_primo(number):

    if number <= 1:
        return False

    else:
        for i in range(2, number):
            if number % i == 0:
                return False

        return True


def numeros_primos():

    numbers = list(range(1, 101))

    primos = []

    for num in numbers:
        if es_primo(num):
            primos.append(num)

    return primos


if __name__ == '__main__':

    print(numeros_primos())
