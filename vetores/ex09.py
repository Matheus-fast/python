n = int(input())

dados = []
botas = []

for i in range(n):
    m, l = input().split()

    dados.append(int(m))
    dados.append(l)
    botas.append(dados[:])
    dados.clear()

print(botas)

for i in botas:
    for j in i:
        
        if type(j) == int:
            vezes_botas = i[:].count(j)

            if botas.count(j) >= 2:
                print('o número é par')

        elif type(j) == str:
            vezes_tamanho = botas[:].count(j)

print(vezes_botas)
print(vezes_tamanho)