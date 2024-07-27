n = int(input())

matriz = [[0 for _ in range(n)] for _ in range(n)]

for linha in range(n):
    matriz[linha] = list(map(int, input().split()))

valores = []

for i in range(n*n):
    valores.append(i+1)

for e, linha in enumerate(matriz):
    for j, coluna in enumerate(linha):
        
        if coluna == 0:
            pos_linha = e+1
            pos_coluna = j+1

        if coluna in valores:
            valores.remove(coluna)

print(valores[0])
print(pos_linha)
print(pos_coluna)