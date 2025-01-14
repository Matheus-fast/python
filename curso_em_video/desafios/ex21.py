from asyncio import events
import pygame

r = str(input('Você quer ouvir uma música?'))

if r == 'sim' :   

    pygame.init()
    pygame.mixer.music.load('tu_es_tudo.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

    pause = str(input('Você quer pausar a música?'))
    if pause == 'sim':
        pygame.mixer.music.pause()

        play = str(input('Você quer voltar a ouvir a música?'))
        if play != 'sim':
            play = str(input('Você quer voltar a ouvir a música?'))
            if play == 'sim':
                pygame.mixer.music.unpause()
                pygame.event.wait

        else:
            pygame.mixer.music.unpause()

    else: 
        pygame.event.wait()
        nada = str(input('Sua música está rodando!'))

nada = str(input('Quer parar de ouvir a música? Aperte ENTER!'))
