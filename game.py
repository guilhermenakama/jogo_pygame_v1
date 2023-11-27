import pygame
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

state = INIT 
while state != QUIT: 
    if state == INIT:
        state = init_screen(screen)
    elif state == GAME:
        state = game_screen(screen)            
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados    
  