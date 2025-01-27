while True:

    print()
    print(f'{"CALCULADORA":^30}')
    print('(1) ADIÇÃO')
    print('(2) SUBTRAÇÃO')
    print('(3) MULTIPLICAÇÃO')
    print('(4) DIVISÃO')

    operador = int(input('Qual operador você quer usar? '))

    n1 = int(input('Qual é o primeiro número? '))
    n2 = int(input('Qual é o segundo número? '))

    if operador == 1:
        print(f'Somando {n1} + {n2}: {n1+n2}')

    elif operador == 2: 
        print(f'Subtraindo {n1} - {n2}: {n1-n2}')

    elif operador == 3:
        print(f'Multiplicando {n1} * {n2}: {n1*n2}')

    elif operador == 4:
        print(f'Dividindo {n1} / {n2}: {n1/n2}')
    
    else:
        print('OPÇÃO INVÁLIDA')


    continuar = str(input('Quer continuar? ')).strip().lower()

    if continuar in 'nnao':
        break