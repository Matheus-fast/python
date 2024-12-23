print('-'*30)
print('{:^30}'.format('LOJA DO BARATAO'))
print('-'*30)

barato = cont = maisMil = total = 0

while True:

    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do Produto: R$'))

    if (cont == 0) or (preco < barato):
        barato = produto
        menor = preco

    if preco > 1000:
        maisMil += 1

    total += preco

    r = ' '
    while r not in 'sn':     
        r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

    if r == 's':
        cont += 1
    else:
        break 


print('-'*15, ' FIM DO PROGRAMA ', '-'*15)
print(f'O total gasto na compra foi : R${total}.')
print(f'Foi feito a compra de {maisMil} custando mais de R$1000.00!')
print(f'E o nome do produto mais barato é: {barato} custando {menor}.')