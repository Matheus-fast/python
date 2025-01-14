matriz = [[0 for _ in range(3)] for _ in range(3)]

for coluna in range(3):
    for linha in range(3):
        matriz[coluna][linha] = int(input(f'Digite um valor para a posição [{coluna}] [{linha}]: '))

for coluna in range(3):
    for linha in range(3):
       print(f'[{matriz[coluna][linha]:^7}]', end=' ') if linha < 2 else print(f'[{matriz[coluna][linha]:^7}]', '\n')
