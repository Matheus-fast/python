n = float(input('Me diga um número qualquer: '))

if (n / 2) % 1: 
    print('\033[35mNúmero ímpar!\033[m')
else:
    print('\033[36mNúmero par!\033[m')