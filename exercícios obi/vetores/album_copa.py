# N total de figurinhas e espaços do album
# M quantas figurinhas já foram compradas
# em M figurinhas, cada linha seguinte vai receber o número de uma figurinha já comprada (X)

n = int(input())
m = int(input())

pos = 0
certo = 0
lista = []

for j in range(m):

    num = int(input())

    if num not in lista:
        certo += 1
        pos = lista
        lista.append(num)

if (n-certo) < 0:
    certo = 0

print(n-certo)