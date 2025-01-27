cpf_valido = []
somar = []
resultado_1 = 0
resultado_2 = 0

# pedindo ao usuário um CPF
cpf_usuario = str(input('Digite um CPF válido: '))

# alterando o CPF para poder manipulá-lo
for numero in cpf_usuario:

    if numero not in '-.':
        numero = int(numero)
        cpf_valido.append(numero)

cpf_gerado = cpf_valido[:9]


# commeçando a descobrir o primeiro dígito
contador_regressivo_1 = 10

for digito in cpf_gerado:
    resultado_1 += digito * contador_regressivo_1
    contador_regressivo_1 -= 1

resultado_1 *= 10
ultimoDigito_1 = resultado_1 % 11

digito_1 = ultimoDigito_1 if ultimoDigito_1 <= 9 else 0

# segundo dígito
cpf_gerado.append(digito_1)

contador_regressivo_2 = 11

for digito in cpf_gerado:
    resultado_2 += digito * contador_regressivo_2
    contador_regressivo_2 -= 1

resultado_2 *= 10
ultimoDigito_2 = resultado_2 % 11

digito_2 = ultimoDigito_2 if ultimoDigito_2 <= 9 else 0

cpf_gerado.append(digito_2)

if cpf_gerado == cpf_valido:
    print(f'O cpf {cpf_usuario} é válido!')

else:
    print(f'O CPF não é válido!')