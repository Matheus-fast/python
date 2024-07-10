frase = str(input()).lower().split()
requerido = str(input()).lower()

cont = 0

for palavra in frase:

    for letra in requerido:

        if letra in palavra:
            cont += 1
            break
            
print(cont)