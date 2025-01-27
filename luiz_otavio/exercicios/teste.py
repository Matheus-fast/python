palavra = 'abcdebb'
palavra_secreta = '*' * len(palavra)

letra = 'b'
nova_letra = 'z'

indice = 0

while indice < len(palavra):
    
    if palavra[indice] == letra:
        palavra_secreta = palavra_secreta.replace(palavra_secreta[indice], nova_letra)
        print(palavra_secreta)
    
    indice += 1