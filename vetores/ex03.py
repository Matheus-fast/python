n = int(input())

lista = input().split(' ')
lista2 = []

for i in range(n):
    x = int(lista[i])
    lista2.append(x)

lista2.sort()

for x in lista2:
    print(x, end=' ')
