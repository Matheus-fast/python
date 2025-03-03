path = r"C:\Users\mathe\Documents\Matheus\programming\python\curso_em_video\desafios\ex115\lib\usuarios\users.txt"

def create_file():

    try:
        with open(path, 'x'):
            print('File created')
            pass

    except Exception as e:
        print(f'ERROR! {e   }')
