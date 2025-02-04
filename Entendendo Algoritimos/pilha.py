# utilizamos a pilha chamada de call stack para entender melhor como funciona um algoritimo que funciona junto com recursão 

def fat(x):

    if x == 1: # se o número for igual a X, ele começa a executar as funções suspensas na pilha, de cima para baixo.
        return x
    
    else: # se o número não for igual a 1, ele entrará na recursão, fazendo com que crie uma espécie de pilha que adiciona chamadas de funções nesta pilha para que elas sejam executadas em ordem.

        return x * (fat(x-1))
    
print(fat(3))