'''
* Reto  # 8
* DECIMAL A BINARIO

* Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''


def decimal_a_binario(decimal: int) -> str:

    cociente = decimal

    binario = ''

    while decimal > 0:

        resto = str(cociente % 2)
        cociente = cociente // 2

        binario += resto

        decimal = decimal // 2

    return binario[::-1]

if __name__ == '__main__':
    print(decimal_a_binario(11))
