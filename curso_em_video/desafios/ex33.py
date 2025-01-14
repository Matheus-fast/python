n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))

if n1 > n2 and n1 > n3:
    print('O maior valor digitado foi: \033[31m{}\033[m'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior valor digitado foi: \033[32m{}\033[m'.format(n2))
else:
    print('O maior valor digitado foi: \033[33m{}\033[m'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor valor digitado foi: \033[34m{}\033[m'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor valor digitado foi: \033[35m{}\033[m'.format(n2))
else:
    print('O menor valor digitado foi: \033[36m{}\033[m'.format(n3))