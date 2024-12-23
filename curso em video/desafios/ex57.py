r = str(input('Informe o seu sexo: [M/F]: ')).lower().strip()

while r not in 'mf':
    r = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F]')).lower().strip()
print('Sexo {} cadastrado com sucesso!'.format(r))