from datetime import date, datetime

nascimento = int(input('Digite o ano do seu nascimento: '))

idade = date.today().year - nascimento

print('O aluno tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')

elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')

elif idade > 14 and idade <=19:
    print('Classificação: JÚNIOR')

elif idade > 19 and idade <= 25:
     print('Classificação: SÊNIOR')

else: 
    print('Classificação: MASTER')