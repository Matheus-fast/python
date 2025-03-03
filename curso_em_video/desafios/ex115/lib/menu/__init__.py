import sys

sys.path.append(r'C:\Users\Mathe\Documents\Programação\python\curso_em_video\desafios\ex115\lib')

from time import sleep
from ..usuarios import *

def ornament(msg):

    tam = 45
    line = '=' * tam

    print(line)
    print(f'{msg:^{tam}}')
    print(line)
    return line

def convertInt():

    while True:

        num = input('\033[33mInsira sua opção: \033[m')

        if num.isalpha():
            print('\033[ERROR! O valor digitado não é um número.\033[m')

        else:
            num = int(num)
            return num

def menu():

    while True:

        line = ornament('MENU PRINCIPAL')

        print('\033[36m1 \033[m - \033[34mVer pessoas cadastradas\033[m')
        print('\033[36m2 \033[m - \033[34mCadastrar nova pessoa\033[m')
        print('\033[36m3 \033[m - \033[34mSair do sistema\033[m')

        print(line, '\n')
            
        while True:

            num = convertInt()

            if num > 3:
                print('\033[ERROR! O valor digitado não é uma opção válida.\033[m')


            if 1 <= num <= 3:
                break

        
        sleep(1)

        if num == 1:
            print()
            ornament(f'CLIENTES CADASTRADOS')
            view_clients()

        if num == 2:
            
            print()
            ornament('CADASTRAR CLIENTE')
            nome = str(input('Nome: '))
            idade = str(input('Idade: '))
            insert_clients(nome, idade)
            print(f'{nome} cadastrado(a) com sucesso.')
            print()

        # parar código
        if num == 3:
            ornament('Saindo do sistema...')
            sleep(1)
            break

        
        sleep(1)

    return num   
