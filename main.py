import pygame
from game_field import draw_grass
import screen
from consts import *
import lior

while WHILE_GAME_POINT:
    draw_grass()
    lior.soldier_movement()
