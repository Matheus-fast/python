n = int(input())

nomes = [0] * n 
lances = [0] * n

for i in range(n):
    nomes[i] = str(input())
    lances[i] = int(input())

maior_lance = lances.index(max(lances))

print(nomes[maior_lance])
print(lances[maior_lance])