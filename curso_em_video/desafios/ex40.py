n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

m = (n1+n2) / 2 

if m > 7: 
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
    print('\033[33mParabéns!\033[m Você foi APROVADO!')

elif m > 5 and m < 7:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
    print('O aluno está de \033[35mRECUPERAÇÃO!\033[m')

else: 
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
    print('O aluno foi \033[31mREPROVADO\033') 