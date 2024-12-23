nome = str(input('Digite o seu nome: '))
peso = float(input('Digite seu peso: (KG)'))
altura = float(input('Digite a sua altura'))

imc = peso / (altura**2)

print('O IMC de {} é de {:.1f}'.format(nome, imc))

if imc<18.5:
    print('Você está abaixo do peso!')

elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')

elif imc >= 25 and imc < 30:
    print('Você está sobrepeso')

elif imc >= 30 and imc < 40:
    print('Você está obeso!')

else:
    print('Obesidade mórbita')