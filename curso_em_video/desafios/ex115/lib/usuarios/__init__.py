import os

diretorio = 'C:/Users/mathe/Documents/Programação/python/curso_em_video/desafios/ex115/lib/usuarios/'
caminho = os.path.join(diretorio, 'usuarios.txt')


def criarArquivo():

    try:
        
        global caminho

        caminho = os.path.join(diretorio, 'usuarios.txt')

        open(caminho, 'wt+')

        print(f'Arquivo {'usuarios.txt'} criado com sucesso!')

    except Exception as e:
        print(f'ERRO! {e}')

    except:
        print('Arquivo já criado!')

def visualizarClientes():

    global caminho

    arquivo = r"C:/Users/mathe/Documents/Programação/python/curso_em_video/desafios/ex115/"

    if not os.path.exists(arquivo):
        criarArquivo()

    try:

        with open(caminho, 'r') as arquivo:
            print(f'{arquivo.read()}')
    
    except Exception as e:
        print(f'ERRO! {e}')

def inserirClientes():

    try:

        open('usuario.txt')
    
    except Exception as e:
        print(f'ERRO! {e}')

    else:
        print('Consegui abrir!')

inserirClientes()