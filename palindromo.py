"""
* Escribe una función que reciba un texto y retorne verdadero o
* falso(Boolean) según sean o no palíndromos.
* Un Palíndromo es una palabra o expresión que es igual si se lee
* de izquierda a derecha que de derecha a izquierda.
* NO se tienen en cuenta los espacios, signos de puntuación y tildes.
* Ejemplo: Ana lleva al oso la avellana.
"""
from string import punctuation


def es_palindromo(text: str) -> bool:
    puntuaciones = [i for i in punctuation + ' ']

    try:
        text = ''.join([i for i in text.lower() if i not in puntuaciones])
        return text == text[::-1]

    except:
        return False


if __name__ == '__main__':
    print(es_palindromo('Ana lleva al oso la avellana'))
