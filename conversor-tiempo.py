'''
* Crea una función que reciba días, horas, minutos y segundos(como enteros)
* y retorne su resultado en milisegundos.
'''


def time_conversor(days: int, hours: int, minutes: int, seconds: int) -> str:

    if any(valor <= 0 for valor in [days, hours, minutes, seconds]):
        raise ValueError(
            'Los valores deben ser positivos, evita poner 0 o un numero negativo')

    return (days * 86400000) + (hours * 3600000) + (minutes * 60000) + (seconds * 1000)


if __name__ == '__main__':
    result = time_conversor(1, 1, 1, 1)
    print(result)
