from consts import *
import pygame as pg
import random
pg.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pg.display.set_mode(size)
pg.display.set_caption("flag game")
screen.fill(GREEN)
pg.display.flip()
# creating Shimi
shimi = pg.image.load(SOLDIER_IMAGE).convert()
shimi = pg.transform.scale(shimi, (60, 90))
shimi.set_colorkey((0, 0, 0))

screen.blit(shimi, [0, 0])
pg.display.flip()

list_a = []
list_b = []

for i in range(1, WINDOW_WIDTH - 50):
    list_a.append(i)
for i in range(1, WINDOW_HEIGHT - 50):
    list_b.append(i)
for bush in range(20):
    a = random.choice(list_a)
    b = random.choice(list_b)

    grass = pg.image.load(GRASS_IMAGE).convert()
    grass.set_colorkey((0, 0, 0))
    screen.blit(grass, [a, b])
    pg.display.flip()

finish = False
while not finish:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = True

