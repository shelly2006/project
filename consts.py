# checking which arrow button is pressed

# import pygame
#
# counter = 0
# x = 0
# y = 0
# location = [x][y]
# events = pygame.event.get()
# for event in events:
#     if event.type == pygame.KEYDOWN:
#
#         if event.key == pygame.K_LEFT:
#             y -= 1
#         elif event.key == pygame.K_RIGHT:
#             y += 1
#         elif event.key == pygame.K_UP:
#             x += 1
#         elif event.key == pygame.K_DOWN:
#             x -= 1
#     elif event.key == pygame.K_RETURN:
#         # mines apears
#             x = 4
# # constant

STARTING_POINT = False
ENDING_POINT = False
WHILE_GAME_POINT = True
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 750
FLAG_IMAGE = 'flag.png'
SOLDIER_IMAGE = 'soldier.png'
GRASS_IMAGE = 'grass.png'
MINE_IMAGE = 'mine.png'
INJURY_IMAGE = 'injury.png'
SOLDIER_DANGER_IMAGE = 'soldier_nigth.png'
GREEN = (12, 101, 37)
BASIC_GREEN = (0, 180, 0)
BLACK = (0, 0, 0)
MINES_AMOUNT = 20
GRASS_AMOUNT = 20