from consts import *
import pygame
import random

# pg.init()
# size = (WINDOW_WIDTH, WINDOW_HEIGHT)
# screen = pg.display.set_mode(size)
# pg.display.set_caption("flag game")
# screen.fill(GREEN)
# pg.display.flip()
#
# # creating Shimi
# shimi = pg.image.load(SOLDIER_IMAGE).convert()
# shimi = pg.transform.scale(shimi, (60, 120))
# shimi.set_colorkey((0, 0, 0))
#
# screen.blit(shimi, [0, 0])
# pg.display.flip()
#
# # creating flag
# flag = pg.image.load(FLAG_IMAGE).convert()
# flag = pg.transform.scale(flag, (90, 120))
# flag.set_colorkey((0, 0, 0))
#
#
# screen.blit(flag, [1410, 630])
# pg.display.flip()
#
# list_a = []
# list_b = []
#
# for i in range(1, WINDOW_WIDTH - 50):
#     list_a.append(i)
# for i in range(1, WINDOW_HEIGHT - 50):
#     list_b.append(i)
# for bush in range(20):
#     a = random.choice(list_a)
#     b = random.choice(list_b)
#
#     grass = pg.image.load(GRASS_IMAGE).convert()
#     grass.set_colorkey((0, 0, 0))
#     screen.blit(grass, [a, b])
#     pg.display.flip()
#
# finish = False
# while not finish:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             finish = True


# matrix for the grass

matrix = []   # creating the matrix og the game
for row in range(25):
    matrix.append([])
for row in matrix:
    for col in range(50):
        row.append(0)
for i in range(GRASS_AMOUNT):   # adding the mines amount
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
screen_mines = pygame.display.set_mode((width, height))


# def

def draw_grid():
    for row in range(25):
        for col in range(50):
            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen_mines, GREEN, (x, y, cell_size, cell_size))
    for row in range(25):
        for col in range(50):
            x = col * cell_size
            y = row * cell_size
            if matrix[row][col] == 'grass.png':
                grass = pygame.image.load(matrix[row][col])
                grass = pygame.transform.scale(grass, (60, 60))
                screen_mines.blit(grass, (x, y))
            if matrix[row][col] == 'soldier.png':  # adding the mines on thr grid
                soldier = pygame.image.load(matrix[row][col])
                soldier = pygame.transform.scale(soldier, (60, 120))
                screen_mines.blit(soldier, (x, y))

            # creating the grid

def update_matrix(matrix, move):
    new_matrix = matrix.deepcopy
    if move == right:
        for row in matrix:
            for col in matrix:
                if new_matrix[row][col] == "body":
                    matrix[row][col + 1] = "body"
                    matrix[row][col] = 0
                if new_matrix[row][col] == "legs":
                    if new_matrix[row][col + 1] == "bomb" or new_matrix[row][col + 1] == "mine.png":
                        return "bomb"
                    else:
                        matrix[row][col + 1] = "legs"
                        matrix[row][col] = 0





# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    draw_grid()

    pygame.display.flip()


