n = int(input())

numeros = []
repetidos = []

for i in range(n):
    numeros.append(int(input()))

maxRep = 0

for j in numeros:    
    if numeros.count(j) >= maxRep:
        maxRep = numeros.count(j)

for j in numeros:
    if numeros.count(j) >= maxRep and j not in repetidos:
        repetidos.append(j)

repetidos.sort()

for j in repetidos:
    print(j, end=' ')