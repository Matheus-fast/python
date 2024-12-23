n = int(input())

a = []
cont = 1
soma = 0

for x in range(n):
    h = int(input())
    a.append(h)
    soma += h

    if soma < 1000000:
        cont +=1

print(cont)