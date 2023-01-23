'''
* Crea una función que sume 2 números y retorne su resultado pasados
* unos segundos.
* - Recibirá por parámetros los 2 números a sumar y los segundos que
*   debe tardar en finalizar su ejecución.
* - Si el lenguaje lo soporta, deberá retornar el resultado de forma
*   asíncrona, es decir, sin detener la ejecución del programa principal.
*   Se podría ejecutar varias veces al mismo tiempo.
'''
from threading import Thread
from time import sleep


def sum_and_sleep(x, y, seconds):

    sleep(seconds)
    result = x + y
    print(result)


if __name__ == '__main__':

    lam_funct = lambda x, y, seconds: sum_and_sleep(x, y, seconds)

    thread1 = Thread(target=lam_funct, args=(5, 5, 5))
    thread2 = Thread(target=lam_funct, args=(10, 10, 10))
    thread3 = Thread(target=lam_funct, args=(2, 2, 2))

    thread1.start()
    thread2.start()
    thread3.start()
    print('La función ha sido llamada')
