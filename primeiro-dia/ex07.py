N = int(input())

lista = input().split(" ")
lista2 = []

for x in range(N):
    i = int(lista[x])
    lista2.append(i)

print(sum(lista2))