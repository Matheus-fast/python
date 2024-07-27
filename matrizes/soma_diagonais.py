matriz = [[0 for _ in range(3)] for _ in range(3)]

for coluna in range(3):
    for linha in range(3):
        matriz[coluna][linha] = int(input())
 
print(f'Diagonal principal: {matriz[0][0] + matriz[1][1] + matriz[2][2]}')
print(f'Diagonal secundária: {matriz[0][2] + matriz[1][1] + matriz[2][0]}')
