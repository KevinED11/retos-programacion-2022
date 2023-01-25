'''
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
 '''

if __name__ == '__main__':
    for num in range(1, 100 + 1):
        print(num)

    numeros = [num for num in range(1, 101)]
    print(numeros)


    contador = 0

    while contador < 101:
        print(contador)
        contador += 1

    def numeros():
        return [num for num in range(1, 101)]


    print(numeros())

    def numeros2():
        return list(range(1, 101))

    print(numeros2())










