import pygame
from utils import *

pygame.init()

pygame.display.set_caption("Tic-Tac-Toe")
screen = pygame.display.set_mode((600, 600))
cell_size = 200
current_player = "X"

game_state = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

run = True
while  run:
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0] // cell_size
    y = mouse_pos[1] // cell_size

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN and game_state[y][x] == " ":
            game_state[y][x] = current_player

            if current_player == "X":
                current_player = "O"
            elif current_player == "O":
                current_player = "X"

    if check_verical(game_state) or check_horizontal(game_state) or check_diagonal(game_state):
        run = False
    
    draw_game_state(game_state, screen, cell_size)
    draw_grid(screen)
    pygame.display.update()

pygame.quit()
