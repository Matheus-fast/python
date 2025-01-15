import os

diretorio = 'C:/Users/mathe/Documents/Programação/python/curso_em_video/desafios/ex115/lib/usuarios/'
caminho = os.path.join(diretorio, 'usuarios.txt')
arquivo = r"C:/Users/mathe/Documents/Programação/python/curso_em_video/desafios/ex115/"

def criarArquivo():

    try:
        
        global caminho

        caminho = os.path.join(diretorio, 'usuarios.txt')

        open(caminho, 'x')

    except Exception as e:
        print(f'ERRO! {e}')


def visualizarClientes():

    global caminho

    arquivo = 'usuarios.txt'
    
    if not os.path.exists(caminho):
        criarArquivo()

    try:    

        with open(caminho, 'r') as arquivo:
            print(f'{arquivo.read()}')
            arquivo.close()

    except Exception as e:
        print(f'ERRO! {e}')

def inserirClientes(nome, idade):

    global caminho

    try:
        with open(caminho, 'a') as arquivo:
            arquivo.write(f'{nome:<20} {idade:>5} anos\n')

    except Exception as e:
        print(f'ERRO! {e}')