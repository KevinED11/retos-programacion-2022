"""
* Simula el funcionamiento de una máquina expendedora creando una operación
* que reciba dinero(array de monedas) y un número que indique la selección
* del producto.
* - El programa retornará el nombre del producto y un array con el dinero
*   de vuelta(con el menor número de monedas).
* - Si el dinero es insuficiente o el número de producto no existe,
*   deberá indicarse con un mensaje y retornar todas las monedas.
* - Si no hay dinero de vuelta, el array se retornará vacío.
* - Para que resulte más simple, trabajaremos en céntimos con monedas
*   de 5, 10, 50, 100 y 200.
* - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""


def maquina_expendedora(dinero: list, number_product: int) -> str and list:

    products: dict[str, int] = {
        "pollo": {"id": 1, "price": 10},
        "pescado": {"id": 2, "price": 50},
        "camarones": {"id": 3, "price": 5},

    }

    choice_product = [i for i in products.values() ]
    
    return choice_product


if __name__ == "__main__":
    print(maquina_expendedora(dinero=[], number_product=1))
