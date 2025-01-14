from os import system
from time import sleep

alunos = []
dado = []

while True:

    dado.append(str(input('Nome: ')))
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))

    alunos.append(dado[:])
    dado.clear()

    r = str(input('Quer continuar? [S/N]')).strip().lower()

    while r not in 'sn':

        print('Resposta diferente de "S" ou "N".')
        r = str(input('Por favor, digite [S/N] para continuar: ')).strip().lower()

    if r == 'n':
        break

system('cls')

while True:

    print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
    print('-'*25)

    for aluno, posicao in enumerate(alunos):
        media = (posicao[1] + posicao[2]) / 2
        print(f'{aluno:<4} {posicao[0]:<10} {media:>8.2f}')
    
    mostrar_nota = int(input('Mostrar notas de qual aluno? (999 INTERROMPE): '))

    if mostrar_nota == 999: 
        break
    else:
        print(f'Notas de {alunos[mostrar_nota][0]} são: {alunos[mostrar_nota][1:]}')
        print('-'*35)

print('FINALIZANDO')
sleep(1)
print('>>>    VOLTE SEMPRE     <<<')