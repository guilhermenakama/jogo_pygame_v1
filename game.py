import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
WIDTH = 1350
HEIGHT = 650
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missão Natal")

# ----- Inicia assets
BARRIER_WIDTH = 50
BARRIER_HEIGHT = 38
HERO_WIDTH = 80
HERO_HEIGHT = 62
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/background.png').convert()
Hero_img = pygame.image.load('assets/img/penguin.png').convert_alpha()
Hero_img = pygame.transform.scale(Hero_img, (HERO_WIDTH, HERO_HEIGHT))

# ----- Inicia estruturas de dados
# Definindo os 
STILL = 0
FALLING = 1
FLYING = 2
GRAVITY = 6

class Hero(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 10
        self.rect.bottom = HEIGHT
        self.speedy = 0

    def update(self):
        # Atualização da posição do jogador
        player.speedy = GRAVITY
        
        if self.state == FLYING:
            player.speedy = -12

        if self.state == STILL:
            player.speedy = 0

        self.rect.y += player.speedy

        # Mantem dentro da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.state = STILL
            self.rect.bottom = HEIGHT

game = True
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
# Criando um jogador
player = Hero(Hero_img)
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
    window.blit(background, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador
    
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados   