def leiaInt(msg):
    
    n = input(msg)

    while True:

        try:
            n = int(n)
            break
        except:    
            n = input(f'\033[0;31mERRO! Digite um número inteiro válido: \033[m')

    return n

def leiaFloat(msg):

    n = input(msg)

    while True:

        try:
            n = float(n)
            print('real')
            break

        except KeyboardInterrupt:
            print('\033[0;31mERRO! O usuário preferiu não digitar nenhum valor real.')
            n = 0

        except:
            n = input(f'\033[0;31mERRO! Digite um número real válido: \033[m')

    return n


int = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {int} e o real foi {real}')
      
