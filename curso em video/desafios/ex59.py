n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

t = False

while not t:
    print("[ 1 ] SOMAR")
    print("[ 2 ] MULTIPLICAR")
    print("[ 3 ] MAIOR")
    print("[ 4 ] NOVOS NÚMEROS")
    print("[ 5 ] SAIR DO PROGRAMA")
    r = int(input(">>>>> Qual é a sua opção? "))

    if r == 5:
        t = True
    
    elif r == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    
    elif r == 3:
        if n1 > n2:
            print('O maior entre eles é: {}'.format(n1))
        else:
            print('O maior entre eles é: {}'.format(n2))
    
    elif r == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    
    elif r == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))

print('Encerrado!')