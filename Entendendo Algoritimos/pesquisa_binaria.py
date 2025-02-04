# A pesquisa binária ela existe para encontar um número específico em uma lista muito grande com poucas tentativas, com uma técnica simples:

# Em uma lista com 100 números, a pessoa escolheu o número 30.

# Para eliminar grande parte das possibilidades, vamos checar o meio da lista. Caso o número digitado for menor que o número do meio da lista, todos os números maiores que o número da metade da lista serão desclassificados, caso contrário, o programa eliminará os menores números.

# No nosso caso, o número 30 é menor que 50, que seria a metade da lista.

# Então, fará a mesma coisa, divindo a lista em dois e checando se o número digitado é maior ou menor que o número da metade da lista, até que ele consiga achar o resultado certo.s


# entendo a lógica
""" def pesquisa_binaria(lista, item):

    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:

        meio = int((alto + baixo) / 2)
        chute = lista[meio]

        if chute == item:
            return meio

        if chute > item:
             alto = meio - 1
        
        else:
            baixo = meio - 1
        
    return None

minha_lista = [-1, 0, 1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 5))
print(pesquisa_binaria(minha_lista, -1)) """


# Fazendo um algoritimo para encontrar um valor em meio a  100 números
def encontar_número_em_lista_de_100(lista, numero_desejado=0):

    menor_numero = 0
    maior_numero = len(lista)
    contador = 0 

    while menor_numero <= maior_numero: # enquanto não tiver somente um item faltando, ele fará o código a seguir

        numero_meio = int((menor_numero + maior_numero) / 2)
        chute = lista[numero_meio] -1 # chute vai receber o valor que está no meio da lista 

        if chute == numero_desejado: # se o valor do chute for igual ao valor desejado, irá acabar.
            return numero_meio, contador

        if numero_meio > numero_desejado: # se o número do meio da lista for maior que o número desejado, então o novo valor do meio será todos os que estiverem acima do valor do meio

            maior_numero = numero_meio 
            contador += 1

        else: # caso contrário, todos os valores abaixo do valor do meio serão considerados, e os que estão acima desconsiderados
            menor_numero = numero_meio 
            contador += 1
    return None
    
    
minha_lista = list(range(1, 101))
print(encontar_número_em_lista_de_100(minha_lista, 10))

