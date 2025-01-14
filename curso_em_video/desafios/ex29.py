velo = int(input('Qual é a velocidade atual do carro? '))

if velo > 80:
    multa = float(velo - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80KM/h\nVocê deve pagar uma multa de \033[31mR${:.2f}!\033[m'.format(multa))

print('Tenha um bom dia e dirija \033[4;33msempre coms segurança!\033[m')