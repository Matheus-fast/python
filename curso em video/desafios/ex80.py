valores = []

for numero in range(0, 5):

    n = int(input('Digite um número: '))

    if numero == 0 or n > max(valores):
        print('Valor adicionado a ultima posição da lista.')
        valores.append(n)
        print(valores)

    else:
        
        pos = 0

        while pos <= len(valores):

            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Valor adicionado a posição {pos}')
                print(valores)
                break
            pos += 1

print('-='*14)
print(valores)
