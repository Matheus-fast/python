'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

num=float(input('Digite um valor: '))
print('O valor digitado foi \033[35m{}\033[m e a sua porção inteira é \033[33m{}\033[m'.format(num, int(num)))