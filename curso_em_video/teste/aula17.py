"""
valores = []

for num in range(0, 5):
    valores.append(int(input('Digite um número a ser adicionado na lista: ')))

for c, v, in enumerate(valores):
    print(f'Achei o número {v} na {c}° posição!')

print('Cheguei ao final da lista')

"""

# existe uma peculiaridade em python na hora de copiar uma lista
"""
a = [1, 2, 3 ,4]
b = a

b[3] = 8

print(a) # esta lista será alterada, pois o python cria uma ligação nas duas listas
print(b) # [1, 2 , 3, 8]

print('-='*15)

a[3] = 4
b[3] = 4

print(a) # voltando a lista ao seu valor inicial
print(b)

print('-='*15)

b = a[:] # com este método, você está copiando a lista A na lista B, sem traçar uma ligação nas duas
b[3] = 8 # e agora você pode conseguir alterar o valor da lista B SEM alterar o valor da lista A

print(a)
print(b)
"""

lista = [1, 2 , 3]

lista.insert(4, 6)
print(lista)