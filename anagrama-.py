'''
* Escribe una función que reciba dos palabras(String) y retorne
* verdadero o falso(Bool) según sean o no anagramas.
* - Un Anagrama consiste en formar una palabra reordenando TODAS
*   las letras de otra palabra inicial.
* - NO hace falta comprobar que ambas palabras existan.
* - Dos palabras exactamente iguales no son anagrama.
'''


def is_anagram(palabra1, palabra2):

    if palabra1.lower() == palabra2.lower():
        return False

    else:
        return sorted(palabra1) == sorted(palabra2)

if __name__ == '__main__':
    print(is_anagram('amor', 'roma'))
