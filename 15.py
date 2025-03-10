#Crear el joc de tres en ratlla i que permeti jugar a un jugador contra la màquina o a dos jugadors.


import pygame
import random
import sys

# Definir constants
X = "X"
O = "O"
EMPTY = None
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
LINE_COLOR = (0, 0, 0)
CIRCLE_RADIUS = 60
CIRCLE_COLOR = (242, 85, 96)
CROSS_WIDTH = 25
CROSS_COLOR = (28, 170, 156)
BACKGROUND_COLOR = (28, 170, 156)

# Inicialitzar pygame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tres en Ratlla")

# Crear el tauler
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

# Funció per dibuixar el tauler
def draw_lines():
    # Dibuixar línies
    pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), LINE_WIDTH)

# Funció per dibuixar les marques (X, O)
def draw_marks():
    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                pygame.draw.line(screen, CROSS_COLOR, (col * WIDTH // 3 + 50, row * HEIGHT // 3 + 50), ((col + 1) * WIDTH // 3 - 50, (row + 1) * HEIGHT // 3 - 50), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, ((col + 1) * WIDTH // 3 - 50, row * HEIGHT // 3 + 50), (col * WIDTH // 3 + 50, (row + 1) * HEIGHT // 3 - 50), CROSS_WIDTH)
            elif board[row][col] == O:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6), CIRCLE_RADIUS, LINE_WIDTH)

# Funció per comprovar si hi ha guanyador
def check_winner(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Funció per comprovar si el tauler està ple
def is_full():
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

# Funció per fer jugada de la màquina (jugada aleatòria)
def ai_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]
    return random.choice(empty_cells)

# Funció per gestionar la interacció del joc
def main():
    player_turn = True  # True si és el torn del jugador, False si és el torn de la màquina
    game_over = False
    game_mode = "1P"  # O "2P" per jugar a dos jugadors

    # Bucle principal del joc
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if player_turn:
                    mouseX, mouseY = event.pos
                    clicked_row = mouseY // (HEIGHT // 3)
                    clicked_col = mouseX // (WIDTH // 3)
                    if board[clicked_row][clicked_col] == EMPTY:
                        board[clicked_row][clicked_col] = X
                        if check_winner(X):
                            game_over = True
                        player_turn = False

            if game_mode == "1P" and not player_turn and not game_over:
                row, col = ai_move()
                board[row][col] = O
                if check_winner(O):
                    game_over = True
                player_turn = True

        screen.fill(BACKGROUND_COLOR)
        draw_lines()
        draw_marks()

        if game_over:
            font = pygame.font.Font(None, 74)
            if check_winner(X):
                text = font.render("Guanya Jugador X", True, (0, 255, 0))
            elif check_winner(O):
                text = font.render("Guanya Jugador O", True, (0, 255, 0))
            else:
                text = font.render("Empat", True, (0, 255, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pygame.display.update()

# Iniciar el joc
if __name__ == "__main__":
    main()
