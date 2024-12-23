salario = float(input('Qual é o salário do funcionário?'))
novoSalario = salario + ( salario * 15 / 100)
print('Um funcionário que ganhava \033[31mR${}\033[m, com \033[32m15% de aumento\033[m, passa a receber \033[33mR${:.2f}\033[m'.format(salario, novoSalario))
