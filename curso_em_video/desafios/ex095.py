time = []
jogador  = {}
gols = []

cod = 0

while True:

    jogador.clear()
    gols.clear()

    cod += 1
    jogador['cod'] = cod
    jogador['nome'] = str(input('Digite o nome do jogador: ')).capitalize().strip()
    partidas = int(input(f'Digite quantas partidas o {jogador["nome"]} jogou: '))

    for i in range(1, partidas+1):

        gol = int(input(f'Digite quantos gols  fez na {i}° partida: '))
        gols.append(gol)

    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())

    while True:

        continuar = str(input('Deseja continuar? [S | N]: ')).lower().strip()

        if continuar not in 'sn':
            print('ERRO!')
            print('Por favor digite apenas S para continuar ou N para encerrar o programa.')      
       
        else:
            break

    if continuar == 'n':
        break

print('-='*30)
print(f'{"TIME":^60}')
print('-='*30)

print(f'{"COD":>5}', end=' ')
print(f'{"NOME":<10}', end='')
print(f'{"GOLS":<20}', end='')
print(f'{"TOTAL":<20}')

print('-'*60)

for jogador in time:

    print(f'{jogador["cod"]:>5}', end=' ')
    print(f'{jogador["nome"]:<10}', end='')
    print(f'{str(jogador["gols"]):<20}', end='')
    print(f'{jogador["total"]:<20}')

print('-'*60)

while True:

    view = int(input('\nMostrar dados de qual jogador?\n(Use o código do Jogador ou 999 para PARAR) '))

    if view != 999:
        
        for jogador in time:

            if jogador['cod'] == view:

                print(f'\n   --- LEVANTAMENTO DO JOGADOR {jogador["nome"].upper()}   ---')

                for j, g in enumerate(jogador['gols']):
                    print(f' => Na {j+1}° partida, fez {g} gols.')

    else:
        break


""" print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(gols):
    print(f'  => Na {i+1}° partida, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols.') """