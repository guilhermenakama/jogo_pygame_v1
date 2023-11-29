import pygame
import random
from assets import *
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL
        self.collided = False  # Adiciona o atributo collided

        self.image = assets[PLAYER_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 10
        self.rect.bottom = HEIGHT
        self.speedy = 0
        self.assets = assets 
        self.frame = 0

    def update(self):
        # Atualização da posição do jogador
        Player.speedy = GRAVITY

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50
        
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

        # Verifica colisão com os pássaros
        #collisions = pygame. sprite.spritecollide(self, True)
        #if collisions:
            # Encerra o programa em caso de colisão
            #self.collided = True
            #Player.reset_player(self)
        
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1 % 2

            # Verifica se já chegou no final da animação.
            # Se ainda não chegou ao fim da explosão, troca de imagem.
            center = self.rect.center
            #self.image = self.rena_anim[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center

    def collide_snows(self, snows_group):
        # Atualização se jogador colidiu com alguma bola de neve
        return pygame.sprite.spritecollide(self, snows_group, False)

    @staticmethod
    def reset_player(player):
        player.state = STILL
        player.rect.centerx = WIDTH / 10
        player.rect.bottom = HEIGHT

            

class Snow(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[SNOW_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - SNOW_WIDTH
        self.rect.y = random.randint( HEIGHT // 10, HEIGHT // 1)
        self.speedx = random.uniform(-6,-2)

    def update(self):
        # Atualizando a posição da bola de neve
        self.rect.x += self.speedx

        # Se a bola de neve passar do final da tela, volta para cima e sorteia novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = WIDTH-SNOW_WIDTH
            self.rect.y = random.randint(0, HEIGHT)
            self.speedx = random.uniform(-6,-2)



