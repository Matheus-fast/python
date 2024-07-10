tamanho = int(input())

lista = list(map(int, input().split()))

lista.sort()

maior_positivo = lista[-1] * lista[-2] * lista[-3]

maior_com_negativo = lista[0] * lista[1] * lista[-1]

negativo = 0

for n in lista:

    if n < 0:
        negativo += 1

if negativo >= 2 and maior_com_negativo > maior_positivo:
    print(maior_com_negativo)
else:
    print(maior_positivo)