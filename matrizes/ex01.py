matriz = [[0 for _ in range(3)] for _ in range(3)]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input())

for e, linha in enumerate(matriz):
    print(f'Linha {e}: {sum(linha)}')
