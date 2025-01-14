from time import sleep

def enfeite():

    enfeite = '-=' * 20
    print(enfeite)

def maior(* num):

    enfeite()

    print('Analisando os valores passados...')
    sleep(0.8)

    for j in num:

        tam = len(j)

        if tam == 0:
            print('Não foram informados números.')
            mai = 0
        
        else:
            mai = max(j)

        for i in j:
            print(i, end=' ')
            sleep(0.4)

    else:
        sleep(0.8)
        print(f'\nAo todo foram informados {tam} números.')
        print(f'E o maior valor informado foi: {mai}')
        

valores = (2, 3, 4, 1)
maior(valores)

valores = (22, 33, 41, 10, 12, 31)
maior(valores)

valores = (22, 3, 10)
maior(valores)

valores = ()
maior(valores)