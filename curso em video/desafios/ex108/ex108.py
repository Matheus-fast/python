import moeda

valor = float(input('Digite o preço: '))

print(f'A metade de {moeda.moeda(valor)} é de: {moeda.moeda(moeda.dobro(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é de: {moeda.moeda(moeda.metade(valor))}')
print(f'Com um acréscimo de 13% sobre {moeda.moeda(valor)}, o novo valor fica: {moeda.moeda(moeda.acrescimo(valor, 13))}')
print(f'E com uma redução de 10% sobre {moeda.moeda(valor)}, o novo valor fica: {moeda.moeda(moeda.diminuir(valor, 10))}')