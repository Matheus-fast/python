from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1;4;35m{} é BISSEXTO\033[m'.format(ano))
else:
    print('O ano \033[1;4;31m{} NÃO é BISSEXTO\033[m'.format(ano))

    