somaIdade = 0
idade = 0
maiorIdade = 0
menos20 = 0

for n in range (1,5):

    print("----- {}° PESSOA -----".format(n))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    if sexo == 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeH = nome

    if sexo == 'F' and idade < 20:
        menos20 += 1

    somaIdade += idade

mIdade = somaIdade / n

print('A média de idade do grupo é de {:.1f} anos'.format(mIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdade, nomeH))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menos20))