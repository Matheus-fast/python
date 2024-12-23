n = int(input())

lista = []
lista = input().split(' ')

a = 0
b = 0

for i in range(n):

    x = int(lista[i])

    if x == 1:              # Irá verificar se o usuário pressionou o interruptor 1, que alterna o estado só da lâmpada A

        if a == 1:          # Irá verificar se a lâmpada está ligada.
            a = 0           # Se estiver, irá desligar
        else:           
            a = 1           # Se não estiver, irá ligar
    
    elif x == 2:            # Caso o usuário digitou o número 2, irá inverter o estado de cada lâmpada (o que é ligado, desliga, o que está desligado liga.)
       
        if a == 1:          # Se a lâmpada "A" estiver ligada, irá desligar
            a = 0
        elif a == 0:        # Se a lâmpada "A" estiver desligada, irá ligar
            a = 1
            
        if b == 1:          # Se a lâmpada "B" estiver ligada, irá desligar
            b = 0
        elif b == 0:        # Se a lâmpada "B" estiver desligada, irá ligar
            b = 1

print(a)                    # Irá falar o estado atual das duas lâmpadas
print(b)