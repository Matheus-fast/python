matriz = [[0 for _ in range(3)] for _ in range(3)]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input())

for linha in matriz:
    for coluna in linha:
        if coluna == matriz[0][0]:
            maior = coluna
        
        if coluna >= maior:
            maior = coluna

for linha in matriz:
    for coluna in linha:
        if coluna == maior:
            print(-1, end=' ')
        else:
            print(coluna, end=' ')
    print()
        