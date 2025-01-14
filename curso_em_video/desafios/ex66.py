n = s = cont = 0

while True:
    n = int(input('Digite um número (999 PARA PARAR):  '))
    if n == 999:
        break
    s += n
    cont += 1 
print(f'A soma dos {cont} números digitados é de: {s}')