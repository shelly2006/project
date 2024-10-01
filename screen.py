


import pygame
import random
from consts import *

pygame.init()

cell_size = 30  # Size of each grid cell

matrix = []  # creating the matrix og the game
for row in range(25):
    matrix.append([])
for row in matrix:
    for col in range(50):
        row.append(0)
for i in range(MINES_AMOUNT):  # adding the mines amount
    keep_going = True
    while keep_going:
        a = random.randint(0, 24)
        b = random.randint(0, 49)
        if b - 1 > 0 and b + 1 < 49:
            matrix[a][b] = 'mine.png'
            matrix[a][b - 1] = "bomb"
            matrix[a][b + 1] = "bomb"
            keep_going = False


def setting_soldier(matrix):
    for row in range(3):
        for col in range(2):
            matrix[row][col] = "body"
    for row in range(3, 4):
        for col in range(2):
            matrix[row][col] = "legs"
    return matrix


def setting_flag(matrix):
    for row in range(21, 25):
        for col in range(47, 50):
            matrix[row][col] = "flag"
    return matrix


rows = len(matrix)
cols = len(matrix[0])
width = cols * cell_size
height = rows * cell_size
screen_mines = pygame.display.set_mode((width, height))

setting_soldier(matrix)
setting_flag(matrix)


def draw_grid():
    for row in range(25):
        for col in range(50):
            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen_mines, BASIC_GREEN, (x, y, cell_size, cell_size), 1)  # creating the grid
            if matrix[row][col] == 'mine.png':  # adding the mines on thr grid
                mine = pygame.image.load(matrix[row][col])
                mine = pygame.transform.scale(mine, (90, 30))
                screen_mines.blit(mine, (x, y))
            if matrix[row][col] == 'body':
                if matrix[row + 3][col + 1] == "legs":
                    danger_soldier = pygame.image.load('soldier_nigth.png')
                    danger_soldier = pygame.transform.scale(danger_soldier, (60, 120))
                    screen_mines.blit(danger_soldier, (x, y))


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen_mines.fill(BLACK)
    draw_grid()
    pygame.display.flip()


