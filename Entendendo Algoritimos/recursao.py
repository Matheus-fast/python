# vamos usar o método de Recursão para fazer uma contagem regressiva sem usar uma estrutura de repetição.

# vale lembrar que não há vantagens em utilizar ou não, apenas é um método que pode ser utilizado.

def contagem_regressiva(x):
    
    print(x)

    if x == 1: # isso é chamado de caso base, que é quando fazemos com que o loop seja parado
        return x

    else:
        contagem_regressiva(x-1) # e aqui é o caso recursivo, quando o loop é executado, chamando a função novamente.

contagem_regressiva(5)