m = 0

for n in range (0,6):
    s = int(input('Digite um número: '))
    if s % 2 == 0:
        m += s
        n += 1
print('A soma dos números pares é {}'.format(m))