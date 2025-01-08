def converterNum(num):

    if ',' in num:

        nova = num.replace(',', '.')
        valorNum = float(nova) 
        
    else:
        valorNum = float(num)
    
    return valorNum

def lerDinheiro(mensagem):

    valor = str(input(mensagem)).strip()

    while True:

        if 'abcdefgijklmnopqrstuvwxyz' in valor:
            print(f'\033[31mERRO! {valor} não é um preço válido!\033[m')
            valor = str(input(mensagem)).strip()
            
        else:
            break
    
    converterNum(valor)

lerDinheiro('digite um número: ')
