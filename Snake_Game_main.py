import pygame
import random
import sys
import json

# Inicializa o Pygame
pygame.init()

# Configurações da tela
pygame.display.set_caption("Snake Game")  # display do nome do jogo
width, height = 900, 600  # tamanho da tela
# tamanho da tela / variavel global
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()  # relogio do jogo / variavel global

# Cores RGB com os parametros ja estipulados por regras de cores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# parametros da cobra
square_size = 20  # tamanho de cada quadrado
snake_speed = 15  # velocidade da cobra a cada iteracao do loop

# Variável para rastrear o estado do jogo
game_state = "menu"  # Estados possíveis: "menu", "jogo"

# Função para desenhar o menu
def show_menu():
    screen.fill(black)
    font = pygame.font.SysFont("Pristina", 35)
    title = font.render("Bem-vindo ao Snake Game!", True, white)
    start_text = font.render("Pressione [Enter] para jogar", True, green)
    quit_text = font.render("Pressione [Esc] para sair", True, red)

    # Exibir textos na tela do menu
    screen.blit(title, (width // 2 - title.get_width() // 2, height // 3))
    screen.blit(start_text, (width // 2 -
                start_text.get_width() // 2, height // 2))
    screen.blit(quit_text, (width // 2 -
                quit_text.get_width() // 2, height // 2 + 60))
    pygame.display.update()

# Funcao para pausar o jogo
def pause_game():
    paused = True
    font = pygame.font.SysFont("Pristina", 35)
    pause_text = font.render("Jogo Pausado - Pressione [Espaço] para continuar", True, white)

    while paused:
        screen.blit(pause_text, (width // 2 - pause_text.get_width() // 2, height // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Despausar o jogo
                    paused = False

# funcao para gerar comida
def food_generator(): # gera o quadrado da comida dentro da tela e alinhado com os movimentos da cobra
    food_x = round(random.randrange(0, width - square_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - square_size) / 20.0) * 20.0
    return food_x, food_y

# funcao para desenhar a comida
def drawing_food(size, food_x, food_y):
    pygame.draw.rect(screen, red, [food_x, food_y, size, size])

# funcao que desenha a cobra
def drawing_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, green, [pixel[0], pixel[1], size, size])

# funcao para contabilizar a pontuacao no ecra de jogo
def score(pontuacao):
    font = pygame.font.SysFont("Pristina", 30)
    text = font.render("Pontuação: " + str(pontuacao), True, white)
    screen.blit(text, [3, 3])

# funcao para direcionar a cobra no jogo


def snake_direction(key):
    if key == pygame.K_DOWN:
        snake_speed_x = 0
        snake_speed_y = square_size
    elif key == pygame.K_UP:
        snake_speed_x = 0
        snake_speed_y = -square_size
    elif key == pygame.K_RIGHT:
        snake_speed_x = square_size
        snake_speed_y = 0
    elif key == pygame.K_LEFT:
        snake_speed_x = -square_size
        snake_speed_y = 0
    return snake_speed_x, snake_speed_y

# funcao principal do jogo


def run_game():
    end_game = False  # declaracao da variavel booleana para o loop

    snake_x = width / 2
    snake_y = height / 2

    snake_speed_x = 0
    snake_speed_y = 0

    snake_size = 1
    pixels = []  # lista para armazenar as posicoes da cobra

    food_x, food_y = food_generator()

    while not end_game:

        screen.fill(black)  # limpa a tela no inicio de cada iteracao do loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Fechar janela
                end_game = True
            elif event.type == pygame.KEYDOWN:  # Processar teclas pressionadas
                if event.key == pygame.K_SPACE:  # Pausar o jogo
                    pause_game()
                elif event.key in (pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT):
                    snake_speed_x, snake_speed_y = snake_direction(event.key)
                elif event.key == pygame.K_ESCAPE:  # ESC retorna ao menu
                    game_state = "menu"
                    return

        # atualizar a posicao da cobra
        snake_x += snake_speed_x
        snake_y += snake_speed_y

        # Teletransporte: verifica os limites da tela e reposiciona no lado oposto
        if snake_x < 0:  # Saiu pela esquerda
            snake_x = width - square_size
        elif snake_x >= width:  # Saiu pela direita
            snake_x = 0
        if snake_y < 0:  # Saiu pelo topo
            snake_y = height - square_size
        elif snake_y >= height:  # Saiu pela parte inferior
            snake_y = 0

        # desenhar cobra
        # adiciona a posicao da cobra na lista
        pixels.append([snake_x, snake_y])
        if len(pixels) > snake_size:  # movimento da cobra / apaga e adiciona pixeis
            del pixels[0]  # apaga o pixel mais antigo

        # verifica se a cobra colidiu com a comida
        if snake_x == food_x and snake_y == food_y:
            snake_size += 1
            food_x, food_y = food_generator()

        # verifica se a cobra colidiu com ela mesma
        for pixel in pixels[:-1]:  # tirar o ultimo pixel da lista / a cabeca da cobra
            if pixel == [snake_x, snake_y]:
                end_game = True

        # desenhar comida
        drawing_food(square_size, food_x, food_y)
        # desenhar cobra
        drawing_snake(square_size, pixels)
        # atualizar pontuacao
        score(snake_size - 1)

        # atualizar tela
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()
    
# Loop do menu principal do jogo
while True:
    if game_state == "menu":
        # Exibir o menu
        show_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter inicia o jogo
                    game_state = "jogo"
                elif event.key == pygame.K_ESCAPE:  # Esc fecha o jogo
                    pygame.quit()
                    sys.exit()

    elif game_state == "jogo":
        run_game()
        # Após terminar o jogo, voltar ao menu
        game_state = "menu"     
