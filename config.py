import pygame
from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
WIDTH = 1024 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define tamanhos
BIRD_WIDTH = 90
BIRD_HEIGHT = 72
PLAYER_WIDTH = 90
PLAYER_HEIGHT = 72

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

# Configurações de jogabilidade
GRAVITY = 4
WORLD_SPEED = -3
INITIAL_BIRDS = 5
FLY_SPEED = -10

# Estados do Player
DONE = 0
PLAYING = 1
STILL = 2
FALLING = 3
FLYING = 4