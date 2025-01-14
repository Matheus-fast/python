
nome = str(input('Digite seu nome completo: ')).strip().split()

print('Muito prazer em te conhecer!')
print('O seu primeiro nome é \033[34m{}\033[m'.format(nome[0]))
print('O seu último nome é \033[33m{}\033[m'.format(nome[len(nome)-1]))