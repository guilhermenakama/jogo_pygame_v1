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
world_sprites = pygame.sprite.Group()
Player = Player(load_assets())

while state != QUIT and game_running: 
    if state == INIT:
        state = init_screen(screen)

    elif state == GAME:
        Player.update()
        state, game_running = game_screen(screen, Player, world_sprites)
        if state == QUIT:
            game_running = False
             
    else:
        state = QUIT

    # Verifica colisão com os pássaros
    if not Player.collided and Player.collide_birds(world_sprites):
        # Define o jogador como colidido
        Player.collided = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            # Aqui você pode adicionar tratamentos de eventos de teclas globais
            pass
        # Reinicia o jogo se o jogador pressionar a tecla "Esc"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            
            Player.reset()  # Se desejar reiniciar o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados    
