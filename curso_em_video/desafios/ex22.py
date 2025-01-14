nome = str(input('Digite o seu nome completo: ')).strip()

n1 = nome.split()

print('Analisando o seu nome...')

print('O seu nome em maiúsculas é \033[33m{}\033[m'.format(nome.upper()))
print('O seu nome em minúsculas é \033[32m{}\033[m'.format(nome.lower()))
print('O seu nome tem ao todo \033[34m{}\033[m letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome é \033[35m{}\033[m e ele têm \033[31m{}\033[m letras'.format(n1[0].capitalize(), len(n1[0])))