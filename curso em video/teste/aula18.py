frutas = ['abacaxi', 'maçã', 'banana']

print(f'Esta é a primeira lista {frutas}')

frutas2 = []
frutas2.append(frutas[:])
print(f'Esta é a segunda lista: {frutas2}')

print('-='*15)

frutas[0] = 'uva'
frutas[1] = 'pera'
frutas[2] = 'melancia'
frutas2.append(frutas)

print(f'Esta é a lista 1 após mudanças: {frutas}')
print(f'Esta é a lista 2 após mudanças: {frutas2}')