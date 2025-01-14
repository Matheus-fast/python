jogador  = {}
gols = []

jogador['nome'] = str(input('Digite o nome do jogador: ')).capitalize().strip()
partidas = int(input(f'Digite quantas partidas o {jogador["nome"]} jogou: '))

for i in range(1, partidas+1):

    gol = int(input(f'Digite quantos gols {jogador["nome"]} fez na {i}° partida: '))
    gols.append(gol)

jogador['gols'] = gols[:]
jogador['total'] = sum(jogador['gols'])

print('-='*25)
print(jogador)
print('-='*25)

for k, v in jogador.items():

    print(f'O campo {k} tem valor: {v}')

print('-='*25)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(gols):
    print(f'  => Na {i+1}° partida, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols.')