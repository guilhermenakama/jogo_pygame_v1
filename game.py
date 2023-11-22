import pygame
import random
from assets import *
from config import *
from sprites import *

# Inicialização do Pygame
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missão Natal")

assets = load_assets()

world_speed = -10

game = True
clock = pygame.time.Clock()

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()

# Criando um jogador
player = Player(assets)
all_sprites.add(player)

# Loop principal do jogo
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_SPACE:
                player.state = FLYING   

        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_SPACE:
                player.state = FALLING

 # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(assets[BACKGROUND_IMG], (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador
    
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados   