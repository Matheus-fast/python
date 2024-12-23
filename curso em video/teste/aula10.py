n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2 

print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >= 6.0 else 'ESTUDE MAIS!')

#if m >= 6.0:
#    print('A sua média foi boa, parabéns!')
#else:
#    print('Sua nota foi ruim! Estude mais!!')