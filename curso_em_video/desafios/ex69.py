maior = homens = menores = total = 0

while True:
    print('-'*25)
    print('   CADASTRE UMA PESSOA   ')
    print('-'*25)

    idade = int(input('IDADE: '))
    sexo = ' '
    
    while sexo not in 'mf':
        sexo = str(input('SEXO [M/F]: ')).strip().lower()
    
    total += 1
    print('-'*25)

    if idade > 18:
        maior += 1
    
    if sexo == 'm':
        homens += 1
    
    if sexo == 'f' and idade < 20:
        menores += 1

    r = ' '

    while r not in 'sn':
        r = str(input('Quer continuar? [S/N]: ')).strip().lower()
    if r == 'n':
        print('-'*25)
        break

print(f'O total de pessoas cadastradas no programa são: {total}')
print(f'Sendo as pessoas com mais de 18 anos: {maior}')
print(f'Os homens cadastrados foram: {homens}')
print(f'E as mulheres com menos de 20 anos são: {menores}')
