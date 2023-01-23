'''
* Crea una función que calcule y retorne cuántos días hay entre dos cadenas
* de texto que representen fechas.
* - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
* - La función recibirá dos String y retornará un Int.
* - La diferencia en días será absoluta(no importa el orden de las fechas).
* - Si una de las dos cadenas de texto no representa una fecha correcta se
*   lanzará una excepción.
'''

from datetime import datetime


def days_between_dates(date1: str, date2: str) -> int:

    try:
        date1_obj = datetime.strptime(date1, '%d/%m/%Y')
        date2_obj = datetime.strptime(date2, '%d/%m/%Y')

    except ValueError:
        raise ValueError("Una de las fechas no tiene el formato correcto")

    return abs((date1_obj - date2_obj).days)


if __name__ == '__main__':
    print(days_between_dates('30/01/2023', '10/01/2023'))
