numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: 

    while True:

        num = int(input('Digite um número de 0 a 20: '))

        if (num<0) or (num>20):
            print('Número inválido!')
            print('-='*15)
        else:
            break

    print(f'O número digitado foi: {(numeros[num]).upper()}')

    continuar = str(input('Você deseja continuar? ')).strip().lower()

    if continuar not in 'ssim':
        break