n1 = int(input('Informe um número: '))

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print('Analisando o número {}'.format(n1))

print('Unidade:\033[31m', u, '\033[m')
print('Dezena:\033[36m', d, '\033[m')
print('Cetena:\033[35m', c, '\033[m')
print('Milhar:\033[34m', m, '\033[m')