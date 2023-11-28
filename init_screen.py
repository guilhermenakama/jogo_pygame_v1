import pygame
import random
from assets import *
from config import *
from os import path


def init_screen(initial_screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets()

    # Carrega o fundo da tela inicial
    background_init = assets[BACKGROUND_INIT_IMG]
    background_init_rect = background_init.get_rect()

    pygame.mixer.music.load('assets/snd/music-box-we-wish-you-a-merry-christmas-79501.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)



    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        state = GAME
                        running = False
           

        # A cada loop, redesenha o fundo e os sprites
        initial_screen.fill(BLACK)
        initial_screen.blit(background_init, background_init_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
