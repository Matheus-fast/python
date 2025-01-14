from datetime import date

maiores = 0
menores = 0 
anoAtual = date.today().year

for n in range (1,8):
    ano = int(input('Em que ano a {}° pessoa nasceu?'.format(n)))
    if (anoAtual-ano) < 18:
        menores += 1
    else:
        maiores += 1
print('Ao todo tivemos {} pessoas maiores de idadde'.format(maiores))
print('E também tivemos {} pessoas menores de idade'.format(menores))