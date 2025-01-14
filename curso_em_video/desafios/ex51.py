print('='*26)
print(' '*2, '10 TERMOS DE UMA PA')
print('='*26)

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
s = p1 + (10 - 1) * r

for n in range (p1, s + r, r):
    print(n, end=' -> ')
    s = s+1

print('FIM')
