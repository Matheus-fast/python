print('='*26)
print(' '*2, '10 TERMOS DE UMA PA')
print('='*26)

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1

while c <= 10:
    print('{} -> '.format(p1), end=' ')
    p1 += r
    c += 1 
print('FIM')