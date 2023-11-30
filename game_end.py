import pygame
import random
from assets import *
from config import *
from os import path
from game_screen import *


def endgame_screen(game_end_screen, score):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets()

    # Carrega o fundo da tela inicial
    background_end = assets[BACKGROUND_END_IMG]
    background_end_rect = background_end.get_rect()

    # Carrega as músicas
    pygame.mixer.music.load('assets/snd/game-over-super-mario-made-with-Voicemod-technology.mp3')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(loops=1)

    text_surface = assets[SCORE_FONT].render('Pontuação final:'"{:08d}".format(score), True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  100)
    background_end.blit(text_surface, text_rect)

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
