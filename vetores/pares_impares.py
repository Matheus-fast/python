pares = []
impares = []

for i in range (0,10):

    n = int(input())

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

for n in pares:
    print(n, end=' ')
print('')
for n in impares:
    print(n, end=' ')