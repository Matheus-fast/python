def notas(*n, sit=False):

    """
            -> Sistema de média de aluno
        :parm n: São as notas fornecidas
        :parm sit: a situação do aluno, sendo possível ser falso ou negativo
        :parm return: retorna um dicionário com as informações do aluno

    """    

    notas = []

    for i in n:

        notas.append(i)
    
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)

    aluno = {
        'total': f'{len(notas)}',
        'maior': f'{maior}',
        'menor': f'{menor}',
        'media': f'{media}',
    }

    if sit:

        if media < 5:
            aluno['situação'] = 'ruim'

        elif media <= 7:
            aluno['situação'] = 'razoavel'  

        else:
            aluno['situação'] = 'boa'  


    print(aluno)

help(notas)
notas(10, 3, 10, 10)