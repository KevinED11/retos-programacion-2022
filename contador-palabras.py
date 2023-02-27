

'''
Reto  # 7
CONTANDO PALABRAS
Dificultad: MEDIA

Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
'''

from string import punctuation


if __name__ == '__main__':

    text = "Hola, esto es un ejemplo. Hola hola HOLA"

    words = text.lower().split()

    counts = {}

    for palabra in words:

        palabra = palabra.strip(punctuation)

        if palabra in counts:
            counts[palabra] += 1

        else:
            counts[palabra] = 1
    
    print(counts)

    for word, count in counts.items():
        print(f'se han encontrado {count} veces/vez la palabra "{word}"')
