"""
* Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
* - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
* - EXTRA: ¿Eres capaz de dibujar más figuras?
"""


def cuadrado(lado1: int) -> str:
    fila = "* " * lado1
    area = [fila for _ in range(lado1)]

    return "\n".join(area)


if __name__ == "__main__":
    print(cuadrado(lado1=6, lado2=6))
