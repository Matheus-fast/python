import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://youtube.com')

except Exception as e:
    print('O site do Curso em Vídeo não está disponível no momento!')
    print(f'Erro: {e}')

else:
    print('O site está acessível!')