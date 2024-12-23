palavras = ('abacaxi', 'uva', 'melancia', 'melao', 'banana', 'laranja', 'mexerica', 'caqui',
            'mamao', 'pera', 'kiwi', 'comer', 'lanchar', 'jantar', 'almocar', 'alimentar', 
            'digerir')

for p in palavras:

    
    print(f'\nA palavra {p.upper()} possui as vogais:', end=' ')

    for l in p:

        if l in 'aeiou':
            print(f'{l}', end=' ')
           

