import random

# from consts import *
# import pygame as pg
#
# BLACK = (0, 0, 0)
# green = (0, 180, 0)
#
#
#
# def main():
#     global SCREEN, CLOCK
#     pg.init()
#     SCREEN = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#     CLOCK = pg.time.Clock()
#     SCREEN.fill(BLACK)
#
#     drawGrid()
#     while True:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#
#
#         pg.display.update()
#
#
# def drawGrid():
#     blockSize = 30 #Set the size of the grid block
#     for x in range(0, WINDOW_WIDTH, blockSize):
#         for y in range(0, WINDOW_HEIGHT, blockSize):
#             rect = pg.Rect(x, y, blockSize, blockSize)
#             pg.draw.rect(SCREEN, green, rect, 1)
#     list_a = []
#     list_b = []
#     for i in range(0, 1470, 30):
#         list_a.append(i)
#     for i in range(0, 720, 30):
#         list_b.append(i)
#     mine = pg.image.load(MINE_IMAGE).convert()
#     mine.set_colorkey((0, 0, 0))
#     for i in range(20):
#         a = random.choice(list_a)
#         b = random.choice(list_b)
#         SCREEN.blit(mine, [a, b])
#         pg.display.flip()
#     shimi_danger = pg.image.load(SOLDIER_DANGER_IMAGE).convert()
#     shimi_danger = pg.transform.scale(shimi_danger, (60, 90))
#     shimi_danger.set_colorkey((0, 0, 0))
#
#     SCREEN.blit(shimi_danger, [0, 0])
#     pg.display.flip()
#
#
# main()





import pygame
import random


pygame.init()


cell_size = 30  # Size of each grid cell

matrix = []
for row in range(25):
    matrix.append([])
for row in matrix:
    for col in range(50):
        row.append(0)
for i in range(20):
    keep_going = True
    while keep_going:
       a = random.randint(0, 24)
       b = random.randint(0, 49)
       if b - 1 > 0 and b + 1 < 49:
           matrix[a][b] = 'mine.png'
           matrix[a][b - 1] = 1
           matrix[a][b + 1] = 1
           keep_going = False

rows = len(matrix)
cols = len(matrix[0])
width = cols * cell_size
height = rows * cell_size
screen = pygame.display.set_mode((width, height))


GREEN = (0, 180, 0)
BLACK = (0, 0, 0)


def draw_grid():
    for row in range(25):
        for col in range(50):
            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen, GREEN, (x, y, cell_size, cell_size), 1)
            if matrix[row][col] == 'mine.png':
                mine = pygame.image.load(matrix[row][col])
                mine = pygame.transform.scale(mine, (90, 30))
                screen.blit(mine, (x, y))


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()

