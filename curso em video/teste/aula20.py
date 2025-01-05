""" def soma(a, b):

    s = a+b
    print(s)

soma(10, 2) """

# empacotamento

""" def contador (* num):

    tamanhoNumeros = len(num)

    print(f'Os valores digitados são: {num} e ao todo são {tamanhoNumeros} números digitados.')

contador(10, 20, 30, 2, 3)
contador(13, 2, 3) """

# desempacotamento

""" def somar(* num):

    soma = 0

    for valor in num:
        soma += valor
    
    print(soma)

somar(2, 4, 5)
somar(2, 4) """

#

""" def dobra(lista):

    pos = 0

    while pos < len(lista):

        lista[pos] *= 2
        pos += 1
    
    print(lista)

valores = [1, 2, 3, 4, 5]
dobra(valores) """