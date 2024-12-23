valores = []
pares = []
impares = []

while True: 

    valores.append(int(input('Digite um número: ')))

    while True:

        r = str(input('Deseja continuar? [S/N]')).lower().strip()

        if r not in 'sn':
            print('Opção inválida!')
        else:
            break

    if r == 'n':
        break

for numero in range(len(valores)):

    if valores[numero] % 2 == 0:
        pares.append(valores[numero])
    else:
        impares.append(valores[numero])
    
print('-='*15)
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')