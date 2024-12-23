from random import choice

primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno ')

sorteado = choice([primeiroAluno, segundoAluno, terceiroAluno, quartoAluno])

print('O aluno escolhido foi \033[33m{}\033[m'.format(sorteado))