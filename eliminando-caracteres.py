"""
* Crea una función que reciba dos cadenas como parámetro(str1, str2)
* e imprima otras dos cadenas como salida(out1, out2).
* - out1 contendrá todos los caracteres presentes en la str1 pero NO
*   estén presentes en str2.
* - out2 contendrá todos los caracteres presentes en la str2 pero NO
*   estén presentes en str1.
"""


def eliminando_caracteres(str1: str, str2: str) -> str:

    out1 = "".join([i for i in str1 if i not in str2])
    out2 = "".join([i for i in str2 if i not in str1])

    print(f'la cadena 1 es "{out1}" y la cadena 2 es "{out2}"')


if __name__ == '__main__':
    eliminando_caracteres('juan', 'alberto')
