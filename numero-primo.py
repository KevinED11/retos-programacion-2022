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
        return False if [i for i in range(2, number) if number % i == 0] else True


def numeros_primos():
    # return list(filter(es_primo, range(1, 101)))
    return [n for n in range(1, 101) if es_primo(n)]


if __name__ == '__main__':
    print(numeros_primos())
