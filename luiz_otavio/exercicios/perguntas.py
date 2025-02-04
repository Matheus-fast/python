perguntas = [

    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['10', '5', '2', '4'],
        'Resposta': '5'
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['5', '15', '35', '25'],
        'Resposta': '25'
    },

    {
        'Pergunta': 'Quanto é 11+11?',
        'Opções': ['10', '2', '22', '21'],
        'Resposta': '22'
    }

]

contador = 0

for pergunta in perguntas:

    for key, value in pergunta.items():

        if key == 'Pergunta':
            print(value)

        if key == 'Opções':
            for alternativas, opcao in enumerate(value):
                print(f'{alternativas+1}) {opcao}')

            while True:

                try:
                    resposta = int(input('Qual a sua alternativa? '))
                    
                    if 1 <= resposta <= 4:
                        break
                    else:
                        print('Alternativa inválida!')

                except:
                    print('Por favor, digite um número válido.')

        if key == 'Resposta':

            verificar_resposta = pergunta['Opções'][resposta-1]

            if verificar_resposta == value:
                print('✅ Parabéns! Você acertou! ✅')
                contador += 1

            else:
                print('❌ Infelizmente você errou! ❌')

print(f'Você acertou {contador} de 3 perguntas.')