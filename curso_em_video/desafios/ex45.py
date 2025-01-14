import random
from time import sleep

print('Suas opções: ')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
r = str(input('Qual é a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

pc = str(random.randint(1,3))

if r == '1':
    r = r.replace('1', 'PEDRA')
elif r == '2':
    r = r.replace('2', 'PAPEL')
elif r == '3':
    r = r.replace('3', 'TESOURA')

if pc == '1': 
    pc = pc.replace('1', 'PEDRA')
elif pc == '2':
    pc = pc.replace('2', 'PAPEL')
elif pc == '3':
    pc = pc.replace('3', 'TESOURA')

print('-='*11)
print('Computador jogou {}'.format(pc))
print('Jogador jogou {}'.format(r))
print('-='*11)

if r == 'PEDRA' and pc == 'PEDRA':
    print('EMPATE!')
elif r == 'PEDRA' and pc == 'PAPEL':
    print('COMPUTADOR VENCE!')
elif r == 'PEDRA' and pc == 'TESOURA':
    print('JOGADOR VENCE!')

elif r == 'PAPEL' and pc == 'PEDRA':
    print('JOGADOR VENCE!')
elif r =='PAPEL' and pc == 'PAPEL':
    print('EMPATE!')
elif r == 'PAPEL' and pc == 'TESOURA':
    print('COMPUTADOR VENCE!')

elif r == 'TESOURA' and pc == 'PEDRA':
    print('COMPUTADOR VENCE')
elif r == 'TESOURA' and pc == 'PAPEL':
    print('JOGADOR VENCE!')
elif r == 'TESOURA' and pc == 'TESOURA':
    print('EMPATE!')

else:
    print('Jogada inválida!')