import random 
from time import sleep
cont = 0

while True:
    
    print('=-'*15)
    print('JOGO PAR OU ÍMPAR COMEÇANDO!')
    print('=-'*15)
    
    nome = str(input('Digite o nome do jogador: ')).capitalize().strip()
    n = int(input('Diga um valor? '))
    r = str(input('Par ou Ímpar? [P/I]')).lower().strip()
    pc = int(random.randint(0, 10))
    soma = 0
    soma = n+pc


    if int(soma % 2 == 0) and r == 'p':
        
        print('-'*25)
        print(f'Você jogou {n}, o computador {pc}. O total deu {soma} e DEU PAR') 
        print('-'*25)
        print('VOCÊ VENCEU!')
        print('-='*15)
        print('Mais uma vez...')
        sleep(1)
        cont += 1

    elif int(soma % 2 == 1) and r == 'i':
        print('-'*25)
        print(f'Você jogou {n}, o computador {pc}. O total deu {soma} e DEU ÍMPAR') 
        print('-'*25)
        print('VOCÊ VENCEU!')
        print('-='*15)
        print('Mais uma vez...')
        sleep(1)
        cont += 1
    
    elif int(soma % 2 == 0) and r == 'i':
        print('-'*25)
        print(f'Você jogou {n}, o computador {pc}. O total deu {soma} e DEU PAR')
        print('VOCÊ PERDEU')
        break

    elif int(soma % 2 == 1) and r == 'p':
        print('-'*25)
        print(f'Você jogou {n}, o computador {pc}. O total deu {soma} e DEU ÍMPAR')
        print('-'*25)
        print('VOCÊ PERDEU')
        break
     
print('-='*15)
print(f'O jogador ganhou {cont} rodadas.')