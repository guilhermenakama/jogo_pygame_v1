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
    assets[BACKGROUND_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpeg')).convert()

    # Carrega os sons do jogo
    return assets