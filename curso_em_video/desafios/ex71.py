print('='*30)
print('{:^30}'.format('BANCO MATHEUS'))
print('='*30)

valor = int(input('Digite o valor que você deseja sacar: R$'))
total = valor
ced = 50
totCed = 0
while True:

    if total >= ced:
        total -= ced
        totCed += 1

    else:   
        
        if totCed > 0:
            print(f'Foram {totCed} cédulas de R${ced} sacadas.')

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        totCed = 0

        if total == 0:
            break

print('='*30)
print('Volte sempre ao BANCO MATHEUS! Tenha um ótimo dia!')
