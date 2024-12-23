from random import randint
from time import sleep

import os

texto = 'JOGUE NA MEGA SENA'

print('-='*30)
print(f'{texto:^50}')
print('-='*30)

jogos = input('Digite o número de jogos que eu sorteie: ').strip()

# vai transformar a quantidade de jogos em int
try:
    quant_jogos = int(jogos)

except:
    print('Você não digitou um número.')

n = 0
numeros = []
matriz = []

print()
print('-='*5, f'SORTEANDO {quant_jogos} JOGOS', '-='*5 )

while n < quant_jogos:

    while len(numeros) < 6:

        num_sorteado = randint(1, 60)
        
        if num_sorteado not in numeros:
            numeros.append(num_sorteado)
        

    matriz.append(numeros[:])
    numeros.clear()

    n += 1

os.system('cls')

for i, l in enumerate(matriz):
    print(f'JOGO {i+1}: {l}')
    sleep(1)
