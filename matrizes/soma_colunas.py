matriz = [[0 for _ in range(3)] for _ in range(3)]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input())

print(f'Coluna 0: {matriz[0][0] + matriz[1][0] + matriz[2][0]}')
print(f'Coluna 1: {matriz[0][1] + matriz[1][1] + matriz[2][1]}')
print(f'Coluna 2: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')




""" primeira = []
segunda = []
terceira = []

for linha in matriz:
    for e, coluna in enumerate(linha):
        if e == 0:
            primeira.append(coluna)
        elif e == 1:
            segunda.append(coluna)
        elif e == 2:
            terceira.append(coluna)

print(f'Coluna 0: {sum(primeira)}')
print(f'Coluna 1: {sum(segunda)}')
print(f'Coluna 2: {sum(terceira)}')

 """