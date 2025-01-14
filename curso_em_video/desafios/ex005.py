n = int(input('Digite um número: '))
s = n+1
a = n-1

print('O valor digitado é {}{}{}, o seu \033[32mantecessor\033[m é {}{}{}, e o seu \033[35msucessor\033[m é {}{}{}'.format('\033[33m', n, '\033[m', '\033[31m', a, '\033[m', '\033[34m', s, '\033[m'))