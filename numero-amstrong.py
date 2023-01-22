'''
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
'''

def is_amstrong(number: int) -> bool:
    result = 0

    if number != int(number):
        return 'Por favor solo coloca numeros enteros'

    for num in str(number):
        num = int(num) ** 3
        result += num

    return result == number

if __name__ == '__main__':
    print(is_amstrong(153))
