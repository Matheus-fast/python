import sys

sys.path.append(r'C:\Users\Mathe\Documents\Programação\python\curso_em_video\desafios\ex115\lib')

from time import sleep
from usuarios import *

def enfeite(msg):

    tam = 45
    linha = '=' * tam

    print(linha)
    print(f'{msg:^{tam}}')
    print(linha)
    return linha

def converterInt():

    while True:

        num = input('\033[33mInsira sua opção: \033[m')

        if num.isalpha():
            print('\033[31mERRO! O valor digitado não é um número.\033[m')

        else:
            num = int(num)
            return num

def menu():

    while True:

        linha = enfeite('MENU PRINCIPAL')

        print('\033[36m1 \033[m - \033[34mVer pessoas cadastradas\033[m')
        print('\033[36m2 \033[m - \033[34mCadastrar nova pessoa\033[m')
        print('\033[36m3 \033[m - \033[34mSair do sistema\033[m')

        print(linha, '\n')
            
        while True:

            num = converterInt()

            if num > 3:
                print('\033[31mERRO! O valor digitado não é uma opção válida.\033[m')


            if 1 <= num <= 3:
                break

        
        sleep(1)

        if num == 1:
            print()
            enfeite(f'CLIENTES CADASTRADOS')
            visualizarClientes()

        if num == 2:
            
            print()
            enfeite('CADASTRAR CLIENTE')
            nome = str(input('Nome: '))
            idade = str(input('Idade: '))
            inserirClientes(nome, idade)
            print(f'{nome} cadastrado(a) com sucesso.')
            print()

        # parar código
        if num == 3:
            enfeite('Saindo do sistema...')
            sleep(1)
            break

        
        sleep(1)

    return num   
