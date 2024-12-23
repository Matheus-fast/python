n1 = float(input('Digite a nota do primeiro aluno: '))
n2 = float(input('Digite a nota do segundo aluno: '))
m = (n1+n2) / 2 
print('A média entre \033[34m{:.1f}\033[m, e \033[35m{:.1f}\033[m, é de: \033[1;32m{:.1f}\033[m'.format(n1, n2, m))