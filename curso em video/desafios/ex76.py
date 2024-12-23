lista = ("Lápis", 1.75,
         "Borracha", 2,
         "Lapiseira", 7,
         "Caderno", 20,
         "Fichário", 120,
         "Marca texto", 6,
         "Caneta Ponta Fina", 6,
         "Estojo", 10
         )

print('-='*23)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-='*23)

for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end = ' ')
    else:
        print(f'R$: {lista[pos]:>6.2f}')
        
print('-='*23)