def enfeite(msg):

    tam = len(msg) + 30
    linha = '-' * tam

    print(linha)
    print(f'{msg:^{tam}}')
    print(linha)

    return linha

while True:

    linha = enfeite('MENU PRINCIPAL')

    print('\033[36m1 \033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[36m2 \033[m - \033[34mCadastrar nova pessoa\033[m')
    print('\033[36m3 \033[m - \033[34mSair do sistema\033[m')

    print(linha)
        
    while True:

        opcao = input('\033[33mInsira sua opção: \033[m')

        if opcao.isalpha():
            print('\033[31mERRO! O valor digitado não é um número.\033[m')

            if not opcao.isalpha():
                print('é um número')
                opcao = int(opcao)
                break

        else:
            opcao = int(opcao)
            break

    while True:

        opcao = input('\033[33mInsira sua opção: \033[m')

        if opcao > 3:
            print('\033[31mERRO! O valor digitado não é uma opção válida.\033[m')
            
        else:
            break        
                


