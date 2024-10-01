import pygame
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

