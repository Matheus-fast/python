def enfeite(msg):

    tam = len(msg) + 4
    enfeite = '~' * tam

    print(enfeite)
    print(f'{msg:^{tam}}')
    print(enfeite)

def PyHelp():
    
    from time import sleep

    print(f'\033[37;41m')
    enfeite('Sistema de Ajuda PyHelp')
    print('\033[m')

    while True:

        biblio = str(input('Função ou biblioteca: ')).lower()

        if biblio == 'fim':
            break
        
        print(f'\033[31;44m')
        enfeite(f'Acessando o manual do comando: {biblio}')
        sleep(1)
        print('\033[m')

        print(f'\033[31;42m')
        print(help(biblio))
        print('\033[m')


PyHelp()