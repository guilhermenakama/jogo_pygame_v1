import pygame
import os
from config import *

BACKGROUND_INIT_IMG = 'background_init'
BACKGROUND_IMG = 'background'
BACKGROUND_END = 'background_end'
PLAYER_IMG = 'player_img'
PLAYER2_IMG='player1_img'
BIRD_IMG = 'snowball_img'
SCORE_FONT = 'score_font'



def load_assets():
    assets = {}

    # Carrega as imagens do jogo
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'player0.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale(assets[PLAYER_IMG], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[BIRD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Snowball.png')).convert_alpha()
    assets[BIRD_IMG] = pygame.transform.scale(assets[BIRD_IMG], (BIRD_WIDTH, BIRD_HEIGHT))
    assets[SCORE_FONT] = pygame.font.Font('assets/fnt/PressStart2P-Regular.ttf', 28)
    
   
    assets[BACKGROUND_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'background.jpg')).convert()
    assets[BACKGROUND_IMG] = pygame.transform.scale(assets[BACKGROUND_IMG], (WIDTH, HEIGHT))
    assets[BACKGROUND_INIT_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'background_init.png')).convert()
    assets[BACKGROUND_INIT_IMG] = pygame.transform.scale(assets[BACKGROUND_INIT_IMG], (WIDTH, HEIGHT))

    assets[BACKGROUND_END] = pygame.image.load(os.path.join(IMG_DIR, 'background_end.png')).convert()
    assets[BACKGROUND_END] = pygame.transform.scale(assets[BACKGROUND_INIT_IMG], (WIDTH, HEIGHT))

    rena_anim = []
    for i in range(2):
        # Os arquivos de animação são numerados de 00 a 08
        filename = 'assets/img/player{}.png'.format(i)
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        rena_anim.append(img)
    assets["rena_anim"] = rena_anim
    
    return assets