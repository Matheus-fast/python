matriz = [[0 for _ in range(3)] for _ in range(3)]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input())

coluna = []
coluna.append(matriz[0][0] + matriz[1][0] + matriz[2][0])
coluna.append(matriz[0][1] + matriz[1][1] + matriz[2][1])
coluna.append(matriz[0][2] + matriz[1][2] + matriz[2][2])

for j in coluna:
    if j == 15:
        colunas = True
    else:
        colunas = False

for e, linha in enumerate(matriz):
    if sum(linha) == 15:
        linhas = True
    else:
        colunas = False

dig = []
dig.append(matriz[0][0] + matriz[1][1] + matriz[2][2])
dig.append(matriz[0][2] + matriz[1][1] + matriz[2][0])

for i in dig:
    if i == 15:
        diagonal = True
    else:
        colunas = False

if colunas:
    if linhas:
        if diagonal:
            print('SIM')
        else:
            print('NAO')
    else:
        print('NAO')
else:
    print('NAO')