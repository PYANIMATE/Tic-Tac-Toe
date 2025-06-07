import pygame

def draw_grid(screen):
    pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 600), 4)
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 4)
    pygame.draw.line(screen, (255, 255, 255), (0, 200), (600, 200), 4)
    pygame.draw.line(screen, (255, 255, 255), (0, 400), (600, 400), 4)

def draw_game_state(game_state, screen, cell_size):
    for y, row in enumerate(game_state):
        for x, cell in enumerate(row):
            if cell == "X":
                pygame.draw.rect(screen, (95, 247, 93), (x * cell_size, y * cell_size, 200, 200))
            elif cell == "O":
                pygame.draw.rect(screen, (241, 73, 123), (x * cell_size, y * cell_size, 200, 200))
            else: continue

def check_verical(game_state):
    for i in range(3):
        if game_state[0][i] == game_state[1][i] == game_state[2][i] and game_state[0][i] != " ":
            print(game_state[0][i], " won the game!")
            return True

def check_horizontal(game_state):
    for i in range(3):
        if game_state[i][0] == game_state[i][1] == game_state[i][2] and game_state[i][0] != " ":
            print(game_state[i][0], " won the game")
            return True

def check_diagonal(game_state):
    if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[1][1] != " ":
        print(game_state[1][1], " won the game")
        return True

    if game_state[0][2] == game_state[1][1] == game_state[2][0] and game_state[1][1] != " ":
        print(game_state[1][1], " won the game")
        return True

