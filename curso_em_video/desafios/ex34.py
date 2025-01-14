sal = float(input('Digite o valor do seu salário: R$'))

if sal <= 1250:
    novoSal = (sal*0.15) + sal
    print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{} agora.'.format('\033[31m', sal, '\033[m', '\033[32m', novoSal, '\033[m'))
else:
    novoSal = (sal*0.10) + sal
    print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{} agora.'.format('\033[34m', sal, '\033[m', '\033[33m', novoSal, '\033[m'))