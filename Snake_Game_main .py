# Bibliotecas necessarias para a aplicacao do jogo
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
brown = (210, 105, 30)

# parametros da cobra
square_size = 20  # tamanho de cada quadrado
snake_speed = 15  # velocidade da cobra a cada iteracao do loop

# Variável para rastrear o estado do jogo
game_state = "menu"  # Estados possíveis: "menu", "jogo"



# MANIPULACAO DO FICHEIRO JSON
JSON_FILE = "users_and_scores.json"
# criar ficheiro json se nao existir
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as file:
        json.dump({"users": [], "scores": {}}, file, indent=4)
#funcao para carregar os dados do ficheiro json
def load_data():
    """Carrega os dados do ficheiro JSON."""
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Score file not found: {JSON_FILE}")
        return {"users": [], "scores": {}}
    except json.JSONDecodeError:
        print(f"Error reading score file: {JSON_FILE}")
        return {"users": [], "scores": {}}
# funcao para guardar os dados no ficheiro json
def save_data(data):
    """Guarda os dados no ficheiro JSON."""
    try:
        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")



# GESTAO DE UTILIZADORES
# Função para adicionar um utilizador
def add_user(user_name):
    """Adiciona um utilizador à lista."""
    if user_name:
        data = load_data()
        if user_name not in data["users"]:
            data["users"].append(user_name)
            data["scores"][user_name] = []  # Initialize empty score list for new user
        save_data(data)
# Função para remover um utilizador
def remove_user(user_name):
    """Remove um utilizador da lista."""
    data = load_data()
    if user_name in data["users"]:
        data["users"].remove(user_name)
        if user_name in data["scores"]:
            del data["scores"][user_name]  # Remove user's scores
    save_data(data)



# GESTAO DE UTILIZADORES E FUNCOES DO MENU "GERIR UTILIZADORES"
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
        # Carregar os dados dos utilizadores apenas quando necessário
        if action == "input" or action == "list":
            data = load_data()
            users = data["users"]

        screen.fill(black)

        # Título do menu
        title_text = font.render("Gerir Utilizadores", True, aqua)
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 4))

        # Exibir menu principal ou confirmação de remoção
        if action == "input":
            # Exibir prompt para digitar o nome
            prompt = font.render("Digite o nome de utilizador:", True, white)
            screen.blit(prompt, (width // 2 - prompt.get_width() // 2, height // 2 - 50))
            user_display = font.render(user_input, True, green)
            screen.blit(user_display, (width // 2 - user_display.get_width() // 2, height // 2))

        elif action == "list":
            # Exibir a lista de utilizadores
            users_list_font = pygame.font.SysFont("Pristina", 25)
            y_offset = height // 2 - 50
            for idx, user in enumerate(users):
                color = green if idx == selected_index else white
                user_text = users_list_font.render(user, True, color)
                screen.blit(user_text, (width // 2 - 100, y_offset + idx * 30))

                # Botão "Apagar"
                delete_color = red if idx == selected_index else white
                delete_text = users_list_font.render("Apagar", True, delete_color)
                screen.blit(delete_text, (width // 2 + 50, y_offset + idx * 30))

        elif action == "confirm":
            # Exibir confirmação para apagar utilizador
            confirm_font = pygame.font.SysFont("Pristina", 28)
            # Nome do utilizador selecionado para apagar
            user_to_remove = users[selected_index]
            confirm_prompt = confirm_font.render(f"Tem certeza que deseja apagar {user_to_remove}?", True, white)
            screen.blit(confirm_prompt, (width // 2 - confirm_prompt.get_width() // 2, height // 2 - 50))

            # Opções de confirmação: "Sim" ou "Não"
            options = ["Sim", "Não"]
            for idx, option in enumerate(options):
                color = green if idx == confirm_selection else white
                option_text = confirm_font.render(option, True, color)
                x_pos = width // 2 - 50 + idx * 100
                screen.blit(option_text, (x_pos, height // 2 + 30))
                
        # Opção "Voltar"
        back_button_font = pygame.font.SysFont("Pristina", 28)
        back_button_rect = None
        back_button_text = back_button_font.render("Voltar", True, red)  # Cor original
        back_button_rect = pygame.Rect(width // 2 - back_button_text.get_width() // 2, height - 100, back_button_text.get_width(), back_button_text.get_height())
        
        # Se o rato  passar sobre o botão "Voltar", mudar a cor para verde
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if back_button_rect.collidepoint(mouse_x, mouse_y):
            back_button_text = back_button_font.render("Voltar", True, green) 
        else:
            back_button_text = back_button_font.render("Voltar", True, red)
            
        screen.blit(back_button_text, back_button_rect)

        # Instruções na parte inferior
        instructions = font.render("Setas: Navegar | Enter: Selecionar | A: Adicionar | Delete: Apagar", True, white)
        screen.blit(instructions, (width // 2 - instructions.get_width() // 2, height - 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Voltar ao menu principal
                    if action == "confirm":
                        action = "list"  # Voltar para a lista sem apagar
                    elif action == "list":
                        action = "input"  # Voltar para o modo de adicionar utilizador
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
                elif action == "confirm":
                    if event.key == pygame.K_LEFT:  # Navegar para "Sim"
                        confirm_selection = (confirm_selection - 1) % 2
                    elif event.key == pygame.K_RIGHT:  # Navegar para "Não"
                        confirm_selection = (confirm_selection + 1) % 2
                    elif event.key == pygame.K_RETURN:
                        if confirm_selection == 0:  # "Sim" selecionado
                            remove_user(users[selected_index])
                            action = "list"  # Voltar para a lista após apagar
                            selected_index = min(selected_index, len(users) - 1)  # Ajustar índice
                        else:  # "Não" selecionado
                            action = "list"  # Voltar para a lista sem apagar

            # Mouse events for navigation (agora restringido ao menu de confirmação)
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if action == "confirm":
                    # Verificar se o mouse está sobre as opções "Sim" ou "Não" de confirmação
                    confirm_rects = [pygame.Rect(width // 2 - 50, height // 2 + 30, 50, 30),
                                     pygame.Rect(width // 2 + 50, height // 2 + 30, 50, 30)]
                    for idx, rect in enumerate(confirm_rects):
                        if rect.collidepoint(mouse_x, mouse_y):
                            confirm_selection = idx  # Destacar a opção "Sim" ou "Não"

                # Caso não esteja no menu de confirmação, não fazer nada com o mouse
                else:
                    # Verificar se o mouse está sobre um utilizador ou botão "Apagar"
                    for idx in range(len(users)):
                        user_rect = pygame.Rect(width // 2 - 150, height // 2 - 50 + idx * 30, 200, 30)
                        delete_rect = pygame.Rect(width // 2 + 100, height // 2 - 50 + idx * 30, 100, 30)

                        if user_rect.collidepoint(mouse_x, mouse_y):
                            selected_index = idx  # Destacar a opção de utilizador
                        elif delete_rect.collidepoint(mouse_x, mouse_y):
                            selected_index = idx  # Destacar a opção de apagar

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clique do botão esquerdo do mouse
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    if back_button_rect.collidepoint(mouse_x, mouse_y):
                        if action == "confirm":
                            action = "list"  # Voltar da confirmação para a lista
                        elif action == "list":
                            action = "input"  # Voltar da lista para o modo de adicionar utilizadores
                        else:
                            return  # Sair do menu de gestão de utilizadores
                                
                    if action == "input":
                        # Check if click is inside the input box for adding user
                        user_rect = pygame.Rect(width // 2 - 150, height // 2 - 50, 300, 30)  # Define the input area
                        if user_rect.collidepoint(mouse_x, mouse_y):
                            if user_input:  # If there is some text input
                                add_user(user_input)  # Add the user
                                action = "list"  # Switch to the list mode after
                            elif not user_input:  # If there is no input
                                action = "list"  # Switch to the list mode after
                                                
                    elif action == "confirm":
                        # Verificar se o clique está nas opções "Sim" ou "Não" de confirmação
                        confirm_rects = [pygame.Rect(width // 2 - 50, height // 2 + 30, 50, 30),
                                         pygame.Rect(width // 2 + 50, height // 2 + 30, 50, 30)]
                        for idx, rect in enumerate(confirm_rects):
                            if rect.collidepoint(mouse_x, mouse_y):
                                confirm_selection = idx  # Selecionar "Sim" ou "Não"
                                if confirm_selection == 0:  # "Sim" selecionado
                                    remove_user(users[selected_index])
                                    action = "list"  # Voltar para a lista após apagar
                                    selected_index = min(selected_index, len(users) - 1)
                                else:  # "Não" selecionado
                                    action = "list"  # Voltar para a lista sem apagar

                    # Caso não esteja no menu de confirmação, o clique não terá efeito
                    else:
                        # Verificar se o clique está em um utilizador ou botão "Apagar"
                        for idx in range(len(users)):
                            user_rect = pygame.Rect(width // 2 - 150, height // 2 - 50 + idx * 30, 200, 30)
                            delete_rect = pygame.Rect(width // 2 + 100, height // 2 - 50 + idx * 30, 100, 30)

                            if user_rect.collidepoint(mouse_x, mouse_y):
                                selected_index = idx  # Selecionar utilizador
                                action = "confirm"  # Ir para a confirmação de apagar
                                confirm_selection = 0  # "Sim" por padrão
                            elif delete_rect.collidepoint(mouse_x, mouse_y):
                                selected_index = idx  # Selecionar a opção de apagar
                                action = "confirm"  # Ir para a confirmação de apagar
                                confirm_selection = 0  # "Sim" por padrão



# CARREGAR UTILIZADORES DO FICHEIRO JSON E "MENU DE SELECÇÃO DE UTILIZADOR"
# Funcao que carrega os utilizadores do ficheiro JSON 
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

# funcao para selecionar o utilizador
def select_user():
    """Exibe um submenu para selecionar o utilizador antes de começar o jogo, com navegação por teclado e rato."""
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
    is_back_selected = False  # Indica se "Voltar" está selecionado

    while True:
        screen.fill(black)
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 4))

        # Pega a posição do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Desenho das opções (utilizadores)
        spacing = 40
        start_y = height // 4 + 80

        for i, user in enumerate(users):
            # Verifica se o mouse está sobre o nome do utilizador
            user_rect = pygame.Rect(width // 2 - option_font.size(user)[0] // 2,
                                    start_y + i * spacing, option_font.size(user)[0], option_font.size(user)[1])

            # Destacar o utilizador se o mouse estiver sobre ele
            if user_rect.collidepoint(mouse_x, mouse_y):
                color = green
                selected_index = i
                is_back_selected = False  # Focar no utilizador, não em "Voltar"
            else:
                color = green if i == selected_index and not is_back_selected else white

            user_text = option_font.render(user, True, color)
            screen.blit(user_text, (width // 2 - user_text.get_width() // 2, start_y + i * spacing))

        # Desenho da opção "Voltar"
        back_text = "Voltar"
        back_y = start_y + len(users) * spacing + 40  # Posicionar "Voltar" abaixo dos utilizadores
        back_rect = pygame.Rect(width // 2 - option_font.size(back_text)[0] // 2,
                                back_y, option_font.size(back_text)[0], option_font.size(back_text)[1])

        # Destacar "Voltar" se o mouse estiver sobre ele
        if back_rect.collidepoint(mouse_x, mouse_y):
            color = green
            is_back_selected = True  # Focar em "Voltar"
        else:
            color = green if is_back_selected else red

        back_surface = option_font.render(back_text, True, color)
        screen.blit(back_surface, (width // 2 - back_surface.get_width() // 2, back_y))

        pygame.display.update()

        # Gerenciar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Navegar para cima
                    if is_back_selected:
                        is_back_selected = False
                        selected_index = len(users) - 1
                    else:
                        selected_index = (selected_index - 1) % len(users)
                elif event.key == pygame.K_DOWN:  # Navegar para baixo
                    if selected_index == len(users) - 1:
                        is_back_selected = True
                    elif is_back_selected:
                        is_back_selected = False
                        selected_index = 0
                    else:
                        selected_index = (selected_index + 1) % len(users)
                elif event.key == pygame.K_RETURN:  # Selecionar opção com Enter
                    if is_back_selected:  # Selecionou "Voltar"
                        return None
                    else:
                        return users[selected_index]  # Retorna o utilizador selecionado
                elif event.key == pygame.K_ESCAPE:  # Voltar ao menu principal
                    return None  # Retorna None para indicar que o jogador não selecionou um utilizador

            elif event.type == pygame.MOUSEMOTION:
                # Verifica se o mouse moveu e altera a seleção dinamicamente
                if back_rect.collidepoint(mouse_x, mouse_y):
                    is_back_selected = True
                else:
                    for i, user in enumerate(users):
                        user_rect = pygame.Rect(width // 2 - option_font.size(user)[0] // 2,
                                                start_y + i * spacing, option_font.size(user)[0], option_font.size(user)[1])
                        if user_rect.collidepoint(mouse_x, mouse_y):
                            selected_index = i
                            is_back_selected = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Se o botão esquerdo do mouse for pressionado
                    if is_back_selected:  # Verifica se "Voltar" foi clicado
                        return None
                    else:
                        return users[selected_index]  # Retorna o utilizador selecionado



# FUNCAO PARA SALVAR PONTUACOES SEGUIDA DA FUNCAO PARA CARREGAR PONTUACOES 
# E UTILIZADORES ASSOCIADOS (FICHEIRO JSON), PARA EXIBIR NO MENU "VER PONTUACOES"#
# Funcao que guarda as pontuacoes
def save_score(user_name, score):
    """Salva a pontuação do jogador."""
     
    if not user_name:
        user_name = "unknown"
       
    try:
        data = load_data()
        
        # Initialize user if not exists
        if user_name not in data["users"]:
            data["users"].append(user_name)
        
        # Initialize scores if not exists
        if user_name not in data["scores"]:
            data["scores"][user_name] = []
        
        # Add the score
        data["scores"][user_name].append(score)
        
        # Save the data
        save_data(data)
        
        
    except Exception as e:
        print(f"Error saving score: {e}")

# Funcao que mostra o menu com a lista de pontuacoes existentes ("VER PONTUACOES")
def view_scores():
    """Exibe as pontuações dos jogadores em uma lista."""
    font = pygame.font.SysFont("Pristina", 30)
    
    while True:
        try:
            # Reload data each time to get latest scores
            data = load_data()
            
            users = data.get("users", [])
            scores = data.get("scores", {})
            
            screen.fill(black)
            
            # Título
            title_text = font.render("Pontuações dos Jogadores", True, aqua)
            screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 4))
            
            if not users:
                no_scores_text = font.render("Nenhuma pontuação registrada", True, white)
                screen.blit(no_scores_text, (width // 2 - no_scores_text.get_width() // 2, height // 2))
            else:
                y_offset = height // 4 + 60
                
                for user in users:
                    user_scores = scores.get(user, [])
                    if user_scores:
                        max_score = max(user_scores)
                        last_score = user_scores[-1]
                        score_text = f"       última:  {last_score} pts      melhor:  {max_score} pts"
                    else:
                        score_text = "Sem pontuações"
                    
                    # Renderizando o nome do usuário em verde
                    user_surface = font.render(user, True, green)  # Cor verde
                    screen.blit(user_surface, (width // 2 - 230, y_offset))  # Alinhe com o restante do texto
                    
                    # Renderizando as pontuações em branco
                    score_surface = font.render(score_text, True, white)
                    screen.blit(score_surface, (width // 2 - 230 + user_surface.get_width() + 10, y_offset))
                    
                    y_offset += 40
            
            # Definindo a área do botão "Voltar"
            back_text = "Voltar"
            back_surface = font.render(back_text, True, red)
            back_rect = back_surface.get_rect(center=(width // 2, height - 50))
            
            # Verificando a posição do mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if back_rect.collidepoint(mouse_x, mouse_y):
                back_surface = font.render(back_text, True, green)  # Cor verde ao passar o mouse
            
            # Exibindo o botão "Voltar"
            screen.blit(back_surface, back_rect)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Voltar ao menu principal
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and back_rect.collidepoint(mouse_x, mouse_y):
                        return  # Voltar ao menu principal ao clicar no botão "Voltar"
                        
        except Exception as e:
            print(f"Error in view_scores: {e}")
            return


# FUNCAO PARA MOSTRAR E GERIR O MENU PRINCIPAL
# Função para desenhar o menu principal
def show_menu():
    """Exibe o menu principal com navegação por setas e seleção por teclado ou rato."""
    screen.fill(black)

    # Configurações das fontes
    title_font = pygame.font.SysFont("Pristina", 50)  # Fonte maior para o título
    option_font = pygame.font.SysFont("Pristina", 30)  # Fonte menor para as opções

    # Título do menu
    title_text = title_font.render("Bem-vindo ao Snake Game!", True, aqua)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 4))

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
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 4))

        # Pega a posição do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Desenho das opções
        for i, option in enumerate(menu_options):
            # Verifica se o mouse está sobre a opção
            option_rect = pygame.Rect(width // 2 - option_font.size(option)[0] // 2,
                                      start_y + i * spacing, option_font.size(option)[0], option_font.size(option)[1])
            
            if option_rect.collidepoint(mouse_x, mouse_y):
                color = green  # Destacar opção se o mouse estiver sobre ela
                selected_index = i  # Atualizar índice selecionado com o mouse
            else:
                # Define a cor: vermelho para "Sair", senão normal (verde ou branco)
                if i == len(menu_options) - 1:  # Última opção é "Sair"
                    color = red if i != selected_index else green
                else:
                    color = green if i == selected_index else white

            option_text = option_font.render(option, True, color)
            screen.blit(option_text, (width // 2 - option_text.get_width() // 2, start_y + i * spacing))

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
                elif event.key == pygame.K_RETURN:  # Selecionar opção com Enter
                    if selected_index == 0:  # Jogar
                        return "play"
                    elif selected_index == 1:  # Gerir utilizadores
                        return "manage_users"
                    elif selected_index == 2:  # Ver pontuações
                        view_scores()
                    elif selected_index == 3:  # Sair
                        pygame.quit()
                        sys.exit()

                elif event.key == pygame.K_ESCAPE:  # Sair do menu
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Se o botão esquerdo do mouse for pressionado
                    # Selecionar a opção clicada com o mouse
                    if selected_index == 0:  # Jogar
                        return "play"
                    elif selected_index == 1:  # Gerir utilizadores
                        return "manage_users"
                    elif selected_index == 2:  # Ver pontuações
                        view_scores()
                    elif selected_index == 3:  # Sair
                        pygame.quit()
                        sys.exit()
    return None  # Should never reach here, but added for completeness


# FUNCOES ADICIONAIS DO JOGO (PAUSA, GAME OVER, PONTUACAO, EXIBIR NOME DE JOGADOR, 
# DESENHAR COBRA, DESENHAR COMIDA, GERADOR DE COMIDA, MOVIMENTO DA COBRA)#
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
                    
# Funcao para exibir mensagem de Game Over
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

# Funcao para exibir o nome do jogador
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


# Funcao para gerar comida
def food_generator():  # gera o quadrado da comida dentro da tela e alinhado com os movimentos da cobra
    food_x = round(random.randrange(0, width - square_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - square_size) / 20.0) * 20.0
    return food_x, food_y

# Funcao para desenhar a comida
def drawing_food(size, food_x, food_y):
    pygame.draw.rect(screen, brown, [food_x, food_y, size, size])

# Funcao que desenha a cobra
def drawing_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, green, [pixel[0], pixel[1], size, size])

# Funcao para direcionar a cobra no jogo
def snake_direction(key):
    snake_speed_x = 0  # Initialize with default values
    snake_speed_y = 0  # Initialize with default values
    
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
    """Função principal do jogo."""
    if not selected_user:
        selected_user = "unknown"
    
    end_game = False
    snake_x = round((width / 2) / square_size) * square_size
    snake_y = round((height / 2) / square_size) * square_size
    snake_speed_x = 0
    snake_speed_y = 0
    snake_size = 1
    pixels = []
    food_x, food_y = food_generator()
    current_score = 0

    # ciclo de jogo
    while not end_game:
        screen.fill(black)
        display_username(selected_user)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                final_score = snake_size - 1
                save_score(selected_user, final_score)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    final_score = snake_size - 1
                    save_score(selected_user, final_score)
                    return
                elif event.key == pygame.K_SPACE:
                    pause_game()
                elif event.key in (pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT):
                    snake_speed_x, snake_speed_y = snake_direction(event.key)

        snake_x += snake_speed_x
        snake_y += snake_speed_y

        # Teletransporte da cobra
        if snake_x < 0:
            snake_x = width - square_size
        elif snake_x >= width:
            snake_x = 0
        if snake_y < 0:
            snake_y = height - square_size
        elif snake_y >= height:
            snake_y = 0

        # Movimento da cobra
        pixels.append([snake_x, snake_y])
        if len(pixels) > snake_size:
            del pixels[0]

        # Colisão com comida
        if snake_x == food_x and snake_y == food_y:
            snake_size += 1
            current_score = snake_size - 1
            food_x, food_y = food_generator()

        # Colisão com a própria cobra
        for pixel in pixels[:-1]:
            if pixel == [snake_x, snake_y]:
                final_score = snake_size - 1
                save_score(selected_user, final_score)
                game_over_message("GAME OVER !")
                return
            
        # Desenhar elementos na tela
        drawing_food(square_size, food_x, food_y)
        drawing_snake(square_size, pixels)
        score(snake_size - 1)
        
        # Atualizar a tela
        pygame.display.update()
        clock.tick(snake_speed)

# Initializa o estado do jogo 
game_state = "menu"

# Main game loop, verifica os estados do jogo
while True:
    if game_state == "menu":
        action = show_menu()  # obter a ação do menu
        if action == "play":
            selected_user = select_user()  # obter o usuário selecionado
            if selected_user:  # apenas executa o jogo se o usuário for selecionado
                run_game(selected_user)  # correr jogo com o usuário selecionado
        elif action == "manage_users":
            manage_users()
        elif action == "quit":
            pygame.quit()
            sys.exit()

    # voltar sempre ao menu após o jogo
    game_state = "menu"
