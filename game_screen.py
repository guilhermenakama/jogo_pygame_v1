import pygame
import random
from assets import *
from config import *
from sprites import *
 
def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets()

    # Carrega o fundo do jogo
    background = assets[BACKGROUND_IMG]
    # Redimensiona o fundo
    background_rect = background.get_rect()

    # Cria Sprite do jogador
    player = Player(assets)
    # Cria um grupo de todos os sprites e adiciona o jogador.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Cria um grupo para guardar somente os sprites do mundo (obstáculos, objetos, etc).
    # Esses sprites vão andar junto com o mundo (fundo)
    world_sprites = pygame.sprite.Group()
    # Cria blocos espalhados em posições aleatórias do mapa
    for i in range(INITIAL_BIRDS):
        bird = Bird(assets)
        world_sprites.add(bird)
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        all_sprites.add(bird)
    
    # Estados do Player
    DONE = 0
    PLAYING = 1
    STILL = 2
    FALLING = 3
    FLYING = 4

    lives = 3

    score = 0

    state = PLAYING

    pygame.mixer.music.load('assets/snd/electronic-rock-king-around-here-15045.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

    while state != DONE:

        clock.tick(FPS)  # Ajusta a velocidade do jogo.

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_SPACE:
                    player.state = FLYING   

            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_SPACE:
                    player.state = FALLING
        
        if pygame.sprite.spritecollide(player, world_sprites, True):
         # Verifica colisão com os pássaros e define jogador como colidido
            player.collided = True

            lives -= 1

            if player.collided == True and lives == 0:
                state = DONE
            

        # Reinicia o jogo se o jogador pressionar a tecla "Esc"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            state = DONE

              # Se desejar reiniciar o jogador

        all_sprites.update()  # Depois de processar os eventos, atualiza a acao de cada sprite e chama o update de cada um.

        # Verifica se algum bloco saiu da janela
        for bird in world_sprites:
            if bird.rect.right < 0:
                # Destrói o pássaro e cria um novo no final da tela
                bird.kill()
                new_bird = Bird(assets)
                all_sprites.add(new_bird)
                world_sprites.add(new_bird)
                

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        # Atualiza a posição da imagem de fundo.
        background_rect.x += WORLD_SPEED

        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if background_rect.right < 0:
            background_rect.x += background_rect.width
            score += 100

        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        screen.blit(background, background_rect)
        # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        screen.blit(background, background_rect2)

        all_sprites.draw(screen)

        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)

        text_surface = assets['score_font'].render(chr(9829) * lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        screen.blit(text_surface, text_rect)

        pygame.display.update()

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()