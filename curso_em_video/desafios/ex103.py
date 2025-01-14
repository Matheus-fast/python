def ficha(nome, gols):

    if nome == '':
        nome = '<desconhecido>'

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0        

    return f'O jogador {nome} fez {gols} gols.'

nome = str(input('Digite seu nome: '))
gols = str(input('Número de Gols: '))

print(ficha(nome, gols))