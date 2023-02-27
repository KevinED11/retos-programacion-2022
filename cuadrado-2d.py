"""
* Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
* - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
* - EXTRA: ¿Eres capaz de dibujar más figuras?
"""


def cuadrado(lado: int) -> str:
    fila = "* " * lado
    area = [fila for _ in range(lado)]

    return "\n".join(area)


if __name__ == "__main__":
    print(cuadrado(lado=5))
