def leiaInt(msg):
    
    n = input(msg)

    while True:

        if n.isnumeric():
            break
        else:
            n = input(f'\033[0;31mERRO! Digite um número válido: \033[m')

    return n

n = leiaInt('Digite um número: ')
print(f'Você digitou o número: {n}')
      
