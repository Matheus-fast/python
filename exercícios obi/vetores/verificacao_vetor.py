import os

n = int(input())

lista1 = []
lista2 = []

for i in range(n):
    valor = int(input())
    lista1.append(valor)

n2 = int(input())

for i in range(n2):
    valor2 = int(input())
    lista2.append(valor2)

os.system('cls')

for i in range(n2):

    if lista2[i] in lista1:
        print('Sim')
    else:
        print('Nao')