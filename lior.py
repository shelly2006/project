import pygame

def soldier_move(row, col):
    location = [row][col]
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                col -= 1
            elif event.key == pygame.K_RIGHT:
                col += 1
            elif event.key == pygame.K_UP:
                row += 1
            elif event.key == pygame.K_DOWN:
                row -= 1

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
