import time
from consts import *
import pygame
import random

# matrix for the grass

matrix = []  # creating the matrix og the game
for row in range(25):
    matrix.append([])
for row in matrix:
    for col in range(50):
        row.append(0)
for i in range(GRASS_AMOUNT):  # adding the mines amount
    keep_going = True
    while keep_going:
        a = random.randint(0, 24)
        b = random.randint(0, 49)
        if b - 1 > 0 and b + 1 < 49:
            matrix[a][b] = 'grass.png'
            matrix[a][b - 1] = 1
            matrix[a][b + 1] = 1
            keep_going = False
matrix[0][0] = 'soldier.png'
matrix[3][0] = "leg1"
matrix[3][1] = "leg2"
matrix[21][47] = "flag"

cell_size = 30

rows = len(matrix)
cols = len(matrix[0])
width = cols * cell_size
height = rows * cell_size
screen_grass = pygame.display.set_mode((width, height))

CUBE = 30
soldier_loc = (0, 0)


# function that creates the game screen (grass)
def draw_grass():
    for row in range(25):
        for col in range(50):
            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen_grass, GREEN, (x, y, cell_size, cell_size))
    for row in range(25):
        for col in range(50):
            x = col * cell_size
            y = row * cell_size
            if matrix[row][col] == 'grass.png':
                grass = pygame.image.load(matrix[row][col])
                grass = pygame.transform.scale(grass, (60, 60))
                screen_grass.blit(grass, (x, y))
            if matrix[row][col] == 'soldier.png':
                soldier = pygame.image.load(matrix[row][col])
                soldier = pygame.transform.scale(soldier, (60, 120))
                screen_grass.blit(soldier, (x, y))

    flag = pygame.image.load('flag.png')
    flag = pygame.transform.scale(flag, (90, 120))
    screen_grass.blit(flag, (630, 1410))

    loc_x = 0
    loc_y = 0
    soldier_movement(loc_x, loc_y)



def soldier_movement(loc_x, loc_y):
    global WHILE_GAME_POINT
    CUBE = 30
    soldier = pygame.image.load('soldier.png')
    soldier = pygame.transform.scale(soldier, (60, 120))
    while WHILE_GAME_POINT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                WHILE_GAME_POINT = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    loc_y -= CUBE
                    screen_grass.blit(soldier, (loc_x, loc_y))
                elif event.key == pygame.K_DOWN:
                    loc_y += CUBE
                    screen_grass.blit(soldier, (loc_x, loc_y))
                elif event.key == pygame.K_LEFT:
                    loc_x -= CUBE
                    screen_grass.blit(soldier, (loc_x, loc_y))
                elif event.key == pygame.K_RIGHT:
                    loc_x += CUBE
                    screen_grass.blit(soldier, (loc_x, loc_y))
                elif event.key == pygame.K_RETURN:
                    import screen
                    screen.draw_grid()
                    time.sleep(1)
                if matrix_check(matrix, loc_x, loc_y):
                    WHILE_GAME_POINT = False
            pygame.display.flip()
            if matrix_check(matrix, loc_x, loc_y):
                    WHILE_GAME_POINT = False



def matrix_check(matrix, locx, locy):
    game_over = False
    while not game_over:
        col_index = locx // 30
        row_index = locy // 30
        if matrix[row_index][col_index] == "bomb" or matrix[row_index][col_index] == "mine.png":
            game_over = True
        if matrix[row_index][col_index] == "flag":
            game_over = True
        return game_over


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw_grass()

    pygame.display.flip()
