import os

secreta = 'meg'
letra_palavra = ''

contador = 0

while True:

    letra_digitada = input('Digite uma letra da palavra oculta: ').lower().strip()

    try: 
        if letra_digitada.isnumeric():
            print(f'{letra_digitada} não é uma letra!')
            continue
        else:
            letra_digitada = str(letra_digitada)

    except:
        print('Não é uma letra válida. Por favor, insira outra.')
        continue

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in secreta:
        letra_palavra += letra_digitada

    palavra_formada = ''

    for letra_secreta in secreta:
        if letra_secreta in letra_palavra:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
        
    contador += 1

    print(palavra_formada)

    if not '*' in palavra_formada:
        break

os.system('cls')
print(f'A palavra secreta era: {palavra_formada} e você demorou {contador} vezes para acertar!')

