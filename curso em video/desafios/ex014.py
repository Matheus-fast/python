temp = float(input('Informe a temperatura em °C: '))
tempNova = ((9*temp)/5)+32
print('A temperatura de \033[31m{}°C\033[m corresponde a \033[36m{:.1f}°F\033[m'.format(temp, tempNova))