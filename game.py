import pygame
import random
from assets import *
from config import *
from sprites import *
from game_screen import *
from init_screen import *

# Inicialização do Pygame
pygame.init() 
pygame.mixer.init()

# ----- Gera tela principal
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missão Natal")

# Loop principal do jogo
game_running = True
state = INIT
while state != QUIT and game_running: 
    if state == INIT:
        state = init_screen(screen)
    elif state == GAME:
        state = game_screen(screen)
    else:
        state = QUIT

    # Verifica colisão com os pássaros
    if not Player.collided and Player.collide_birds(World_sprites):
        # Define o jogador como colidido
        Player.collided = True
        # game_running = False  # Não encerra o jogo aqui

        # Reinicia o jogo se o jogador pressionar a tecla "Esc"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            game_running = False
            Player.reset()  # Se desejar reiniciar o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados    
