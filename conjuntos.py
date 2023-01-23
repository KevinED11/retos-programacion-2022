'''
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 '''

def conjuntos(array1: list, array2: list, booleano: bool) -> list:

   return [i for i in array1 if i not in array2] if not booleano else [i for i in array1 if i in array2]


if __name__ == '__main__':
    print(conjuntos([1, 2, 3, 4, 7], [1, 2, 4, 7], False))