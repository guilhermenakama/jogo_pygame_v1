import pygame
import random
from assets import *
from config import *
from os import path
from game_screen import *


def endgame_screen(game_end_screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets()

    # Carrega o fundo da tela inicial
    background_end = assets[BACKGROUND_END_IMG]
    background_end_rect = background_end.get_rect()

    pygame.mixer.music.load('assets/snd/music-box-we-wish-you-a-merry-christmas-79501.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)


    state = GAMEOVER

    while state == GAMEOVER:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = INIT
                    

        # A cada loop, redesenha o fundo e os sprites
        game_end_screen.fill(BLACK)
        game_end_screen.blit(background_end, background_end_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
