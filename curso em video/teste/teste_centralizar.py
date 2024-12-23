""" fruta = 'abacaxi'

print(f'{fruta:^30}') """

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
terceira = []

for coluna in range(3):
    for linha in range(3):
        print(f'[{matriz[coluna][linha]:^7}]', end=' ')

    print(matriz[coluna][linha])
    print(coluna, linha)

    print()


print(matriz[:][2])
print(sum(matriz[:][2]))
