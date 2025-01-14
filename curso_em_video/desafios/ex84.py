pessoas = []
dado = []
pesadas = []
leves = []

while True:
    
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    pessoas.append(dado[:])
    dado.clear()

    r = str(input('Deseja continuar? [S/N]')).strip().lower()

    while r not in 'sn':
        print('Opção inválida! Tente novamente.')
        r = str(input('Deseja continuar? [S/N]')).strip().lower()

    if r == 'n':
        break

for n, e in pessoas:

    if n == pessoas[0][0]:
        maior = e
        menor = e

    if e >= maior:
        maior = e

    if e <= menor:
        menor = e

for n, e in pessoas:

    if e >= maior:
        pesadas.append(n)
    elif e <= menor:
        leves.append(n)


print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.2f}Kg. As pessoas com esse peso foram: {pesadas}')
print(f'O menor peso foi de {menor:.2f}Kg. As pessoas com esse peso foram: {leves}')
