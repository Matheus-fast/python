valores = []
r = ''

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

valores.sort(reverse=True)

print(f'Você digitou {len(valores)} valores')
print(f'Os valores em ordem decrescente são: {valores}')

if 5 in valores:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não faz parte da lista.')