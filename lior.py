import pygame as pg
from consts import *

CUBE = 30
soldier_loc = (0, 0)
def soldier_movement():

    while WHILE_GAME_POINT == True:
        for event in pg.event.get():
            soldier_loc = list(soldier_loc)
            if event.type == pg.QOIT:
                WHILE_GAME_POINT = False
            elif event.type == pg.KEYDOWN:
                if event.k == pg.K_UP:
                    soldier_loc[0] -= CUBE
                    return "up"
                elif event.k == pg.K_DOWN:
                    soldier_loc[0] += CUBE
                    return "down"
                elif event.k == pg.K_LEFT:
                    soldier_loc[1] -= CUBE
                    return "left"
                elif event.k == pg.K_RIGHT:
                    soldier_loc += CUBE
                    return "right"
                soldier_loc = tuple(soldier_loc)












def showing_mines():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:



def finish_screen():



#משתנים

flag_locations = "flag"
soldier_legs1 = matrix[3][0]
soldier_legs2 = matrix[3][1]
soldier = matrix[0][0]
mines_locations = "mine.png" or 1
