"""
* Crea una función que ordene y retorne una matriz de números.
* - La función recibirá un listado(por ejemplo[2, 4, 6, 8, 9]) y un parámetro
*   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
*   o de mayor a menor.
"""


def ordenar_list(numeros: list[int] = [1, 2, 3, 4, 5], modo: str = "Desc") -> list[int]:
    modo = modo.lower()
    if modo not in ["asc", "desc"]:
        raise ValueError("El argumento proporcionado es invalido")
    if modo == "asc":
        return sorted(numeros)
    else:
        return sorted(numeros, reverse=True)


if __name__ == "__main__":
    print(ordenar_list(modo="asc"))
