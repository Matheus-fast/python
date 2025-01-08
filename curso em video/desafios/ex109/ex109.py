import moeda

valor = float(input('Digite o preço: '))

print(f'A metade de {moeda.moeda(valor)} é de: {moeda.dobro(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é de: {moeda.metade(valor, True)}')
print(f'Com um acréscimo de 13% sobre {moeda.moeda(valor)}, o novo valor fica: {moeda.acrescimo(valor, 13, True)}')
print(f'E com uma redução de 10% sobre {moeda.moeda(valor)}, o novo valor fica: {moeda.diminuir(valor, 10, True)}')