m = float(input('Digite uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A media de \033[31m{}m\033[m corresponde a \n\033[32m{}km\033[m \n\033[33m{}hm\033[m \n\033[34m{}dam\033[m \n\033[35m{}dm\033[m \n\033[36m{}cm\033[m \n\033[37m{}mm\033[m'.format(m, km, hm, dam, dm, cm, mm))