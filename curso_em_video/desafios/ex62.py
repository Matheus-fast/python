print('='*26)
print(' '*2, '10 TERMOS DE UMA PA')
print('='*26)

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais

    while c <= total:
        print('{} -> '.format(p1), end=' ')
        p1 += r
        c += 1 
    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))


print('Progressão finalizada com {} termos mostrados!'.format(total))