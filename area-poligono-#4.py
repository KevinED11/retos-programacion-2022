'''
* Reto  # 4
* ÁREA DE UN POLÍGONO

* Enunciado: Crea UNA ÚNICA FUNCIÓN(importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
* - La función recibirá por parámetro sólo UN polígono a la vez.
* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
* - Imprime el cálculo del área de un polígono de cada tipo.
*
'''


def calcular_area(poligono: str = 'cuadrado', lado1: int = 4, lado2: int = 0):

    match poligono:

        case 'triangulo':
            return (lado1 * lado2) / 2

        case 'rectangulo':
            return (lado1 * lado2)

        case 'cuadrado':
            return lado1 ** 2

    return 'polígono no soportado'


if __name__ == '__main__':

    # Cálculo del área de un triángulo
    area = calcular_area("triangulo", 6, 8)
    print(area)  # Imprime 24

    # Cálculo del área de un cuadrado
    area = calcular_area("cuadrado", 5)
    print(area)  # Imprime 25

    # Cálculo del área de un rectángulo
    area = calcular_area("rectangulo", 6, 8)
    print(area)  # Imprime 48

    # polígono no soportado
    area = calcular_area("pentagono", 6, 8)
    print(area)
