import os

matriz = [[0 for _ in range(3)] for _ in range(3)]
pares = []
soma = []



for coluna in range(3):
    for linha in range(3):
        matriz[coluna][linha] = int(input(f'Digite o valora da posiçao {[coluna, linha]}: '))
    
os.system('cls')

for coluna in range(3):
    for linha in range(3):
        print(f'[{matriz[coluna][linha]:^7}]', end=' ')

        if matriz[coluna][linha] % 2 == 0:
            pares.append(matriz[coluna][linha])

        if linha == 2:
            soma.append(matriz[coluna][linha])
    print()




print('-='*30)
print(f'A soma dos números pares digitados é: {sum(pares)}')
print(f'A soma dos valores da terceira coluna é: {sum(soma)}')
print(f'O maior valor digitado da segunda linha é: {max(matriz[:][1])}')