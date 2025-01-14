from time import sleep
from random import randint

def sortear():

    print('Sorteando 5 valores da lista: ', end='')

    valores = [randint(1, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]

    for i in valores:
        sleep(0.6)
        print(i, end=' ')
    
    print('PRONTO!')

    return valores

def somarPares(valores):

    print(f'Somando os valores de: {valores} temos: ', end= '')

    soma = 0

    for numero in valores:

        if numero % 2 == 0:
            soma += numero

    sleep(1)
    print(f'{soma}.')

valores = sortear()
somarPares(valores)