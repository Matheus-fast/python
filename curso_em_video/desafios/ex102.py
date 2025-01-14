def fatorial(n, show=False):

    '''
    
        -> Função para saber o Fatorial de um número e a conta utilizada para fazê-la.

    :param n: O número para consulta de Fatorial.
    :param show: A conta para fazer o fatorial, sendo o padrão FALSE. Não mostrando a conta.
    :param return: o retorno do código em uma variável

    '''

    fatorial = 1

    for i in range(n, 0, -1):
        
        fatorial *= i

        if show:

            print(f'{i}', end='')

            if i > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')

    print(f'{fatorial}')

    return fatorial

print(fatorial(5, show=True))
print(help(fatorial))