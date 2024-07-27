n = int(input())

matriz = [[0 for _ in range(n)] for _ in range(n)]
matriz_auxiliar = [[0 for _ in range(n)] for _ in range(n)]

for linha in range(n):
    matriz[linha] = list(map(int, input().split()))

for linha in range(n):
    matriz_auxiliar[linha] = list(map(int, input().split()))

for pos_linha, linha in enumerate(matriz_auxiliar):
    for pos_coluna, coluna in enumerate(linha):

        for pos_linha_aux, linha_auxiliar in enumerate(matriz):
            for pos_col_aux, coluna_auxiliar in enumerate(linha_auxiliar):

                if pos_linha_aux == pos_linha and pos_col_aux == pos_coluna:
                    matriz[pos_linha][pos_coluna] += coluna
                    break    
    
for linha in matriz:
    for coluna in linha:
        print(coluna, end=' ')
    print()