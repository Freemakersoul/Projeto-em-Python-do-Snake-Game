import pygame
import random
import sys
import json
import os


# PARAMETROS INICIAIS DO JOGO
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
aqua = (0, 255, 255)

# parametros da cobra
square_size = 20  # tamanho de cada quadrado
snake_speed = 15  # velocidade da cobra a cada iteracao do loop

# Variável para rastrear o estado do jogo
game_state = "menu"  # Estados possíveis: "menu", "jogo"


# MANIPULACAO DE FICHEIROS JSON
JSON_FILE = "users_and_scores.json"

if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as file:
        json.dump({"users": {}, "scores": []}, file)

# Funcao que carrega os dados do ficheiro JSON
def load_data():
    with open(JSON_FILE, "r") as file:
        return json.load(file)

# variaveis globais para os dados do ficheiro JSON
data = load_data()


users = data["users"]

# Funcao que salva os dados no ficheiro JSON
def save_data(data):
    """Guarda os dados no ficheiro JSON."""
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Função para adicionar um utilizador
def add_user(user_name):
    """Adiciona um utilizador à lista."""
    if user_name:
        data = load_data()
        if user_name not in data["users"]:
            data["users"].append(user_name)
        save_data(data)

# Função para remover um utilizador
def remove_user(user_name):
    """Remove um utilizador da lista."""
    data = load_data()
    if user_name in data["users"]:
        data["users"].remove(user_name)
    save_data(data)


# GESTAO DE UTILIZADORES E FUNCOES DO MENU
# Função para gerir utilizadores
def manage_users():
    """Gestão de utilizadores: adicionar ou remover."""
    font = pygame.font.SysFont("Pristina", 30)
    user_input = ""
    selected_index = 0
    action = "input"  # Estado inicial é "input" (adicionar utilizadores)
    confirm_selection = 0
    screen.fill(black)

    data = load_data()
    global users

    while True:
        data = load_data()
        users = data["users"]

        screen.fill(black)

        # Título do menu
        title_text = font.render("Gerir Utilizadores", True, aqua)
        screen.blit(title_text, (width // 2 -
                    title_text.get_width() // 2, height // 4))

        if action == "input":
            # Exibir prompt para digitar o nome
            prompt = font.render("Digite o nome de utilizador:", True, white)
            screen.blit(
                prompt, (width // 2 - prompt.get_width() // 2, height // 2 - 50))
            user_display = font.render(user_input, True, green)
            screen.blit(user_display, (width // 2 -
                        user_display.get_width() // 2, height // 2))
        elif action == "list":
            # Exibir a lista de utilizadores
            users_list_font = pygame.font.SysFont("Pristina", 25)
            y_offset = height // 2 - 50
            for idx, user in enumerate(users):
                color = green if idx == selected_index else white
                user_text = users_list_font.render(user, True, color)
                screen.blit(user_text, (width // 2 - 150, y_offset + idx * 30))

                # Botão "Apagar"
                delete_color = red if idx == selected_index else white
                delete_text = users_list_font.render(
                    "Apagar", True, delete_color)
                screen.blit(delete_text, (width // 2 +
                            100, y_offset + idx * 30))
        elif action == "confirm":
            # Confirmação para apagar utilizador
            confirm_font = pygame.font.SysFont("Pristina", 28)
            confirm_prompt = confirm_font.render(
                f"Tem certeza que deseja apagar {users[selected_index]}?", True, white
            )
            screen.blit(confirm_prompt, (width // 2 -
                        confirm_prompt.get_width() // 2, height // 2 - 50))

            # Opções de confirmação
            options = ["Sim", "Não"]
            for idx, option in enumerate(options):
                color = green if idx == confirm_selection else white
                option_text = confirm_font.render(option, True, color)
                x_pos = width // 2 - 50 + idx * 100
                screen.blit(option_text, (x_pos, height // 2 + 30))

        # Instruções na parte inferior
        instructions = font.render(
            "Setas: Navegar | Enter: Selecionar | Esc: Voltar | A: Adicionar | Delete: Apagar", True, white
        )
        screen.blit(instructions, (width // 2 -
                    instructions.get_width() // 2, height - 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Voltar ao menu principal
                    if action == "confirm":
                        action = "list"  # Voltar para a lista sem apagar
                    else:
                        return
                elif action == "input":
                    if event.key == pygame.K_RETURN:  # Adicionar utilizador
                        if user_input:
                            add_user(user_input)
                            user_input = ""  # Limpar o campo de entrada
                        action = "list"  # Mudar para o modo de lista
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.key == pygame.K_DELETE:
                        action = "list"  # Ir para a lista ao pressionar DELETE
                    else:
                        user_input += event.unicode
                elif action == "list":
                    if event.key == pygame.K_UP:  # Navegar para cima
                        selected_index = (selected_index - 1) % len(users)
                    elif event.key == pygame.K_DOWN:  # Navegar para baixo
                        selected_index = (selected_index + 1) % len(users)
                    elif event.key == pygame.K_RETURN:  # Selecionar apagar
                        if users:  # Certificar que há utilizadores na lista
                            action = "confirm"  # Mudar para o estado de confirmação
                            confirm_selection = 0  # Selecionar "Sim" por padrão
                    elif event.key == pygame.K_a:  # Voltar para adicionar um utilizador
                        action = "input"
                    elif event.key == pygame.K_DELETE:  # Ir para o menu de remover
                        pass  # Já estamos no estado de lista
                elif action == "confirm":
                    if event.key == pygame.K_LEFT:  # Navegar para "Sim"
                        confirm_selection = (confirm_selection - 1) % 2
                    elif event.key == pygame.K_RIGHT:  # Navegar para "Não"
                        confirm_selection = (confirm_selection + 1) % 2
                    elif event.key == pygame.K_RETURN:
                        if confirm_selection == 0:  # "Sim" selecionado
                            remove_user(users[selected_index])
                            action = "list"  # Voltar para a lista após apagar
                            selected_index = min(selected_index, len(
                                users) - 1)  # Ajustar índice
                        else:  # "Não" selecionado
                            action = "list"  # Voltar para a lista sem apagar

def save_score(user_name, score):
        data = load_data()
        if user_name in data["users"]:
            user_index = data["users"].index(user_name)
            while len(data["scores"]) <= user_index:
                # Garante que o índice existe na lista de pontuações
                data["scores"].append([])
            # Adiciona a pontuação ao jogador
            data["scores"][user_index].append(score)
        else:
            # Caso o usuário não esteja na lista, adicione-o como "unknown"
            if "unknown" not in data["users"]:
                data["users"].append("unknown")
                data["scores"].append([score])
            else:
                unknown_index = data["users"].index("unknown")
                data["scores"][unknown_index].append(score)

        save_data(data)
        

def view_scores():
    """Exibe as pontuações dos jogadores em uma lista."""
    font = pygame.font.SysFont("Pristina", 30)

    # Carregar os dados do arquivo JSON
    data = load_data()
    users = data["users"]
    scores = data["scores"]

    screen.fill(black)

    # Título
    title_text = font.render("Pontuações dos Jogadores", True, aqua)
    screen.blit(title_text, (width // 2 -
                title_text.get_width() // 2, height // 4))

    y_offset = height // 4 + 60  # Espaço inicial para a lista de pontuações

    # Exibir os jogadores e suas pontuações
    for idx, user in enumerate(users):
        user_scores = scores[idx] if idx < len(scores) else []
        user_score_text = font.render(
            f"{user}: {user_scores} pontos", True, white)
        screen.blit(user_score_text, (width // 2 -
                    user_score_text.get_width() // 2, y_offset + idx * 40))

    # Instruções para voltar ao menu
    instructions = font.render("Esc: Voltar ao menu", True, white)
    screen.blit(instructions, (width // 2 -
                instructions.get_width() // 2, height - 50))

    pygame.display.update()

    # Gerenciar eventos
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Voltar ao menu principal
                    return


def load_users_from_json(file_path="users_and_scores.json"):
    """Carrega a lista de utilizadores de um ficheiro JSON."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            # Retorna a lista de utilizadores ou ["Unknown"] por padrão
            return data.get("users", ["unknown"])
    except FileNotFoundError:
        # Caso o ficheiro não exista, retorna apenas o utilizador padrão
        return ["unknown"]
    except json.JSONDecodeError:
        print("Erro ao decodificar o ficheiro JSON. Verifique o formato.")
        return ["unknown"]


def select_user():
    """Exibe um submenu para selecionar o utilizador antes de começar o jogo."""
    # Configurações iniciais
    title_font = pygame.font.SysFont("Pristina", 40)
    option_font = pygame.font.SysFont("Pristina", 30)

    # Título do submenu
    title_text = title_font.render("Selecione o utilizador:", True, aqua)

    # Carregar utilizadores do ficheiro JSON
    users = load_users_from_json()
    if not users:  # Garantir que existe ao menos "unknown"
        users = ["unknown"]

    selected_index = 0  # Índice da opção selecionada

    while True:
        screen.fill(black)
        screen.blit(title_text, (width // 2 -
                    title_text.get_width() // 2, height // 4))

        # Desenho das opções
        spacing = 40
        start_y = height // 4 + 80

        for i, user in enumerate(users):
            color = green if i == selected_index else white
            user_text = option_font.render(user, True, color)
            screen.blit(user_text, (width // 2 -
                        user_text.get_width() // 2, start_y + i * spacing))

        pygame.display.update()

        # Gerenciar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Navegar para cima
                    selected_index = (selected_index - 1) % len(users)
                elif event.key == pygame.K_DOWN:  # Navegar para baixo
                    selected_index = (selected_index + 1) % len(users)
                elif event.key == pygame.K_RETURN:  # Selecionar utilizador
                    return users[selected_index]
                elif event.key == pygame.K_ESCAPE:  # Voltar ao menu principal
                    return None


# MENU PRINCIPAL
# Função para desenhar o menu principal
def show_menu():
    """Exibe o menu principal com navegação por setas e seleção."""
    screen.fill(black)

    # Configurações das fontes
    title_font = pygame.font.SysFont(
        "Pristina", 50)  # Fonte maior para o título
    option_font = pygame.font.SysFont(
        "Pristina", 30)  # Fonte menor para as opções

    # Título do menu
    title_text = title_font.render("Bem-vindo ao Snake Game!", True, aqua)
    screen.blit(title_text, (width // 2 -
                title_text.get_width() // 2, height // 4))

    # Opções do menu
    menu_options = [
        "Jogar",
        "Gerir utilizadores",
        "Ver pontuações",
        "Sair",
    ]

    # Espaçamento vertical entre as opções
    spacing = 40
    start_y = height // 4 + 80

    selected_index = 0  # Índice da opção selecionada

    while True:
        screen.fill(black)
        screen.blit(title_text, (width // 2 -
                    title_text.get_width() // 2, height // 4))

        # Desenho das opções
        for i, option in enumerate(menu_options):
            # Cor diferente para a opção selecionada
            color = green if i == selected_index else white
            option_text = option_font.render(option, True, color)
            screen.blit(option_text, (width // 2 -
                        option_text.get_width() // 2, start_y + i * spacing))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Navegar para cima
                    selected_index = (selected_index - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:  # Navegar para baixo
                    selected_index = (selected_index + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:  # Selecionar opção
                    if selected_index == 0:  # Jogar
                        selected_user = select_user()
                        if selected_user:  # Verifica se um utilizador foi selecionado
                            screen.fill(black)
                            run_game(selected_user)
                    elif selected_index == 1:  # Gerir utilizadores
                        manage_users()
                    elif selected_index == 2:  # ver pontuações
                        view_scores()
                    elif selected_index == 3:  # Sair
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_ESCAPE:  # Sair do menu
                    pygame.quit()
                    sys.exit()

# Funcao para pausar o jogo
def pause_game():
    paused = True
    font = pygame.font.SysFont("Pristina", 30)
    pause_text = font.render(
        "Jogo Pausado - Pressione [Espaço] para continuar", True, white)

    while paused:
        # para ficar centrado a tela
        screen.blit(pause_text, (width // 2 -
                    pause_text.get_width() // 2, height // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Despausar o jogo
                    paused = False


def game_over_message(message):
    """Exibe uma mensagem de Game Over e espera interação."""
    font = pygame.font.SysFont("Pristina", 50)
    screen.fill(black)
    game_over_text = font.render(message, True, red)
    prompt_text = font.render(
        "Pressione [Enter] para voltar ao menu", True, white)
    screen.blit(game_over_text, (width // 2 -
                game_over_text.get_width() // 2, height // 2 - 50))
    screen.blit(prompt_text, (width // 2 -
                prompt_text.get_width() // 2, height // 2 + 20))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Voltar ao menu


def display_username(selected_user):
    """Exibe o nome do utilizador no canto superior direito."""
    font = pygame.font.SysFont("Pristina", 30)

    # Texto "Jogador:" em branco
    text_player = font.render("Jogador:", True, white)
    # Nome do jogador em verde
    text_username = font.render(selected_user, True, green)
    # Calculando a posição para exibir o texto no canto superior direito
    padding = 10  # Distância da borda direita
    # Posição do "Jogador:" (a partir da borda direita)
    player_x = width - padding - text_player.get_width() - text_username.get_width() - \
        10  # Subtraímos a largura do nome do usuário e algum espaço
    # Posição do nome do jogador
    username_x = width - padding - text_username.get_width()
    # Exibindo "Jogador:" e o nome do jogador na tela
    screen.blit(text_player, (player_x, 3))  # "Jogador:" posicionado à direita
    # Nome do usuário posicionado à direita de "Jogador:"
    screen.blit(text_username, (username_x, 3))

# funcao para contabilizar a pontuacao no ecra de jogo


def score(pontuacao):
    font = pygame.font.SysFont("Pristina", 30)
    text = font.render("Pontuação: " + str(pontuacao), True, white)
    screen.blit(text, [3, 3])



# PARAMETROS DA COBRA E DA COMIDA
# funcao para gerar comida
def food_generator():  # gera o quadrado da comida dentro da tela e alinhado com os movimentos da cobra
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


# CONSTRUCAO DO JOGO / COMPONENTES DO JOGO
# funcao principal do jogo
def run_game(selected_user):
    end_game = False  # declaracao da variavel booleana para o loop

    # garante que as posições iniciais da cobra estejam alinhadas aos múltiplos de square_size
    snake_x = round((width / 2) / square_size) * square_size
    # garante que as posições iniciais da cobra estejam alinhadas aos múltiplos de square_size
    snake_y = round((height / 2) / square_size) * square_size

    snake_speed_x = 0
    snake_speed_y = 0

    snake_size = 1
    pixels = []  # lista para armazenar as posicoes da cobra

    food_x, food_y = food_generator()

    while not end_game:
        screen.fill(black)
        display_username(selected_user)  # Mostra o nome selecionado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Retornar ao menu
                    return
                elif event.key == pygame.K_SPACE:  # Pausar o jogo
                    pause_game()
                elif event.key in (pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT):
                    snake_speed_x, snake_speed_y = snake_direction(event.key)

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
                game_over_message("GAME OVER !")
                return

        # desenhar comida
        drawing_food(square_size, food_x, food_y)
        # desenhar cobra
        drawing_snake(square_size, pixels)
        # atualiza a pontuacao
        score(snake_size - 1)

        # atualizar tela
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

    save_data(data)  # Salva os dados
    save_score(data)  # Salva as pontuações

if game_state == "menu":
    show_menu()  # Exibe o menu uma vez
# Loop do menu principal do jogo
while True:
    if game_state == "menu":
        action = show_menu()  # Recebe a ação escolhida no menu
        if action == "play":
            game_state = "jogo"
            current_user = None  # Joga como 'unknown'
        elif action == "manage_users":
            current_user = manage_users()
        elif action == "quit":
            pygame.quit()
            sys.exit()
    elif game_state == "jogo":
        run_game()
        # Após terminar o jogo, voltar ao menu
        game_over_message("GAME OVER !")
        game_state = "menu"
