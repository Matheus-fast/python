n = int(input())

numeros = []
repetidos = []

for i in range(n):

    j = int(input())
    numeros.append(j)

    if j<0 or j>12:
        break

    if (numeros.count(j)) > 1:
        if j not in repetidos:
            repetidos.append(j)

repetidos.sort()

for k in repetidos:
    print(k, end=' ')