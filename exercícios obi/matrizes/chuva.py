n = int(input())

matriz = [[0 for _ in range(n)] for _ in range(n)]
matriz_auxiliar = [[0 for _ in range(n)] for _ in range(n)]

for linha in range(n):
    matriz[linha] = list(map(int, input().split()))

for linha in range(n):
    matriz_auxiliar[linha] = list(map(int, input().split()))

for pos_linha, linha in enumerate(matriz):
    for pos_coluna, coluna in enumerate(linha):
        matriz[pos_linha][pos_coluna] += matriz_auxiliar[pos_linha][pos_coluna]

for linha in matriz:
    for coluna in linha:
        print(coluna, end=' ')
    print()