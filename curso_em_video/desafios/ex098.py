from time import sleep
from operator import neg

def enfeite():

    enfeite = '-=' * 20
    print(enfeite)

def contador(inicio, fim, passo):

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if passo == 0:
        passo = 1

    if inicio > fim:

        if passo >= 1:
            passo = neg(passo)

        fim -= 1
        for i in range(inicio, fim, passo):
            print(i, end=' ')
            sleep(0.2)

    else: 
        
        fim += 1
        for i in range(inicio, fim, passo):
            print(i, end=' ')
            sleep(0.2)
            
    print('FIM!')

enfeite()
contador(1, 10, 1)

enfeite()
contador(10, 0, 2)

enfeite()
print('Agora é sua vez de personalizar a contagem!')

print()

inicio = int(input('INÍCIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))

contador(inicio, fim, passo)