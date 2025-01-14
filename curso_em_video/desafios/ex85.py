numeros = []

for n in range(1,8):

    j = (int(input(f'Digite o {n}° número: ')))

    if n == 1:
        numeros.append([])
        numeros.append([])

    if j % 2 == 0:
        numeros[0].append(j)
    else:
        numeros[1].append(j)

numeros[0].sort()
numeros[1].sort()

print(f'Os valores pares digitados foram: {numeros[0][:]}')
print(f'Os valores ímpares digitados foram: {numeros[1][:]}')