n = int(input())

lista = []
lista2 = []
sum = 0

for x in range(n):
    lista = input().split(' ')
    a = int(lista[0])
    b = int(lista[1])

    if a>b:
        sum += b

print(sum)