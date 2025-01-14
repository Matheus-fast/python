import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

n1 = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)

n = random.randint(0,5)

if n1 == n:
    print('\033[33mPARABÉNS! Você conseguiu me vencer!\033[m')
elif n1 > 5:
    print('Número inválido!')
else:
    print('\033[31mPERDEU!\033[m Eu pensei no número \033[35m{}\033[m e não no \033[36m{}\033[m'.format(n, n1))