import pygame
import random
from assets import *
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        super().__init__()
        self.collided = False

        pygame.sprite.Sprite.__init__(self)
        self.state = STILL
        self.collided = False 

        self.image = assets[PLAYER_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.bottom = int(HEIGHT * 0.8)
        self.speedy = 0
        self.collided = False
        self.assets = assets 

    def update(self):
        # Atualização da posição do jogador
        self.speedy = GRAVITY
    
        if self.state == FLYING:
            Player.speedy = FLY_SPEED
        if self.state == STILL:
            Player.speedy = 0

        self.rect.y += Player.speedy

        # Mantem dentro da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.state = STILL
            self.rect.bottom = HEIGHT

    def collide_birds(self, birds_group):
        return pygame.sprite.spritecollide(self, birds_group, False, pygame.sprite.collide_rect)
    
    def reset(self):
        self.collided = False


class Bird(pygame.sprite.Sprite):
    def __init__(self, assets):
        super().__init__()
        # Construtor da classe mãe (Sprite).

        self.image = assets[BIRD_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - BIRD_WIDTH
        self.rect.y = random.randint( HEIGHT // 4, HEIGHT // 1.5)
        self.speedx = random.randint(-3, -1)

    def update(self):
        # Atualizando a posição do pássaro
        self.rect.x += self.speedx

        # Se o pássaro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = WIDTH-BIRD_WIDTH
            self.rect.y = random.randint(0, HEIGHT)
            self.speedx = random.randint(-1,-1)