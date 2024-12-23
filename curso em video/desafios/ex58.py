import random
from time import sleep

print('Sou seu computador.\nAcabei de pensar em um número entre 0 e 10.\nVocê consegue adivinhar?')

n1 = int(input('Qual é o seu palpite? '))

n = random.randint(0,10)
t = 1

while n1 != n:
    t += 1

    if n1 > 10:
        print('Número inválido!')
        n1 = int(input('Qual é o seu palpite?'))

    elif n < n1:
        print('O numéro que eu pensei é menor')
        n1 = int(input('Qual é o seu palpite?'))

    elif n > n1:
        print('O número que eu pensei é maior')
        n1 = int(input('Qual é o seu outro palpite?'))
        
if n1 == n:
    print('\033[33mPARABÉNS! Você conseguiu me vencer em {} tentativas!\033[m'.format(t))


"""import random
from time import sleep

print('Sou seu computador.\nAcabei de pensar em um número entre 0 e 10.\nVocê consegue adivinhar?')

acertou = False
n = random.randint(0,10)
t = 0

while not acertou:
    n1 = int(input('Qual é o seu palpite? '))
    t += 1

    if n1 > 10:
        print('Número inválido!')

    elif n1 == n:
        acertou = True

    elif n < n1:
        print('O numéro que eu pensei é menor')

    elif n > n1:
        print('O número que eu pensei é maior')
         
print('\033[33mPARABÉNS! Você conseguiu me vencer em {} tentativas!\033[m'.format(t))"""