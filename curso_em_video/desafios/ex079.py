lista = []

while True:

    n = int(input('Digite um número: '))

    while n in lista:
        print('Número não adicionado. Tente novamente...')
        n = int(input('Digite um número: '))

    lista.append(n)
    print('Valor adicionado com SUCESSO!')
    
    r = str(input('Deseja continuar? [S/N] ')).lower().strip()

    while r not in 'ns':
        if r not in 'ns':
            print('COMANDO INVÁLIDO. TENTE NOVAMENTE')
            r = str(input('Deseja continuar? [S/N] ')).lower().strip()

    if r == 'n':
        break    

print('-='*15)
lista.sort()
print(lista)
