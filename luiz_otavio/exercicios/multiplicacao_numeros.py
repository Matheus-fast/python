# exercício para treinar empacotamento e desempacotamento

def multiplicar(*numeros): # aqui os números são recebidos em uma tupla com uma lista dentro, já que eu defini uma lista lá embaixo.

    multi = 1

    for i in numeros: # fiz um for para entrar na primeira tupla
        for j in i: # outro for para entrar na lista e visualizar os números individualmente
            multi *= j

        return multi 

numeros = [1, 2, 3, 4, 5]
multiplicado = multiplicar(numeros)
print(multiplicado)

