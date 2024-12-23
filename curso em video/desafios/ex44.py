preco = float(input('Digite o valor da compra: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista no dinheiro / cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] parcelado em 2x no cartão')
print('[ 4 ] 3 ou mais vezes no cartão')
r = int(input('Qual é a opção? '))

if r == 1:
    desconto = preco - (preco / 100) * 10
    print('O valor do produto é: {}'.format(preco))
    print('O valor à ser pago com desconto de 10% vai ser: {:.2f}'.format(desconto))

elif r == 2:
    desconto = preco - (preco / 100) * 5
    print('O valor do produto é: {}'.format(preco))
    print('O valor à ser pago com desconto de 5% vai ser: {:.2f}'.format(desconto))

elif r == 3:
    print('O valor à ser pago sem desconto vai ser: {:.2f}'.format(preco))

elif r == 4:
    parcelas = int(input('Quantas parcelas serão? '))
    aumento = preco + (preco / 100) * 20
    total = aumento / parcelas
    print('O valor do produto com juros custará: R${}'.format(aumento))
    print('O valor à ser pago em cada parcela custará: R${}'.format(total))

else:
    print('Opção inválida de pagamento!')
    