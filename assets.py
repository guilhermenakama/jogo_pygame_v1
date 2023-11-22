import pygame
import os
from config import *


BACKGROUND_IMG = 'background'
PLAYER_IMG = 'player_img'
BIRD_IMG = 'bird_img'

def load_assets():
    assets = {}

    # Carrega as imagens do jogo
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'penguin.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale(assets[PLAYER_IMG], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[BIRD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bird.png')).convert()
    assets[BIRD_IMG] = pygame.transform.scale(assets[BIRD_IMG], (BIRD_WIDTH, BIRD_HEIGHT))
    assets[BACKGROUND_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'background_atualizado2.jpg')).convert()
    assets[BACKGROUND_IMG] = pygame.transform.scale(assets[BACKGROUND_IMG], (WIDTH, HEIGHT))
    assets[BACKGROUND_IMG] = BACKGROUND_IMG.get_rect()

    # Carrega os sons do jogo
    return assets