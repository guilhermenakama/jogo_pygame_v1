import pygame
import random
from assets import *
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL

        self.image = assets[PLAYER_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 10
        self.rect.bottom = HEIGHT
        self.speedy = 0
        self.assets = assets 

    def update(self):
        # Atualização da posição do jogador
        Player.speedy = GRAVITY
    
        if self.state == FLYING:
            Player.speedy = -6
        if self.state == STILL:
            Player.speedy = 0

        self.rect.y += Player.speedy

        # Mantem dentro da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.state = STILL
            self.rect.bottom = HEIGHT


class Bird(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BIRD_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - BIRD_WIDTH)
        self.rect.y = random.randint(-100, -BIRD_HEIGHT)
        self.speedx = random.randint(-3, 3)

    def update(self):
        # Atualizando a posição do pássaro
        self.rect.x += self.speedx

        # Se o pássaro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-BIRD_WIDTH)
            self.rect.y = random.randint(-100, -BIRD_HEIGHT)
            self.speedx = random.randint(-3, 3)