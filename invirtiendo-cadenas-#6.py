'''
Reto  # 6
* INVIRTIENDO CADENAS*
* Enunciado: Crea un programa que invierta el orden de una cadena de texto.
* - Si le pasamos "Hola mundo" nos retornaría "odnum aloh"
'''


def cadena_invertida(text: str) -> str:

    invertida = ''

    for letra in range(len(text.lower()) - 1, -1, -1):
        invertida += text[letra]

    return invertida


def invertir_cadena(text: str) -> str:

    invertida = text.lower()[::-1]

    return invertida


if __name__ == '__main__':
    print(cadena_invertida('hola mundo'))

    print(invertir_cadena('hola mundo'))
