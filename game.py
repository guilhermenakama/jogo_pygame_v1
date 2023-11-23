import pygame
import random
from os import path

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
img_dir = path.join(path.dirname(__file__), 'img')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

world_speed = -10

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Hero(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 10
        self.rect.bottom = HEIGHT / 2
        self.speedy = 0

    def update(self):
        # Atualização da posição do jogador
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

game = True
clock = pygame.time.Clock()
FPS = 100

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
# Criando um jogador
player = Hero(Hero_img)
all_sprites.add(player)

gravity = 1
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
                player.speedy -= 4
        else:
            player.speedy += gravity


 # Atualizando a posição 
    all_sprites.update()
    def load_assets(img_dir):
        assets = {}
        assets[Hero_img] = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
        assets[background] = pygame.image.load(path.join(img_dir, 'background.png')).convert()
        return assets

    def game_screen(screen):
        # Variável para o ajuste de velocidade
        clock = pygame.time.Clock()
            # Carrega assets
    assets = load_assets(img_dir)

    # Carrega o fundo do jogo
    backgrounds = assets[background]
    background_rects = []
    for background in backgrounds:
        background_rects.append(background.get_rect())

    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:
 # Ajusta a velocidade do jogo.
        clock.tick(FPS)
# Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
# Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
    # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)        

# Atualiza a posição da imagem de fundo.
        background_rects.x += world_speed
        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if background_rects.right < 0:
            background_rects.x += background_rects.width
        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        screen.blit(background, background_rects)
        # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
        background_rect2 = background_rects.copy()
        background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)

        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador
    
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados   
