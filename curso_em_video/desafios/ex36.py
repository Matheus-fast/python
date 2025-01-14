valorCasa = float(input('Qual o valor da casa: R$'))
salario = int(input('Quanto é o seu salário: R$'))
parcelamento = int(input('Quantos anos que você quer pagar? '))

prestacao = valorCasa / (parcelamento * 12)
condicao = prestacao * 100 / 30

print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(valorCasa, parcelamento, prestacao))

if condicao > salario:
    print('Empréstimo \033[31mNEGADO!\033[m')
else:
    print('Empréstimo \033[33mACEITO!\033[m')