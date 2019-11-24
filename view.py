# -------------------------------------------------------------------------
# Developed by:
# Andrés Hernández: linkhl09
# Felipe Parra: Parr0sky
# -------------------------------------------------------------------------

import numpy as np
import pygame
import sys
from pygame.locals import *

# -------------------------------------------------------------------------
# Constraints.
# -------------------------------------------------------------------------

# RGB Values
Aqua = (0, 255, 255)
Black = (0, 0, 0)
Blue = (0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = (0, 128, 0)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
Navy_Blue = (0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)
saddleBrown = (139, 69, 19)

# Button border positions
# btt_b1 = [(550, 100), (700, 100), (700, 150), (550, 150)]
# btt_b2 = [(550, 200), (700, 200), (700, 250), (550, 250)]
# Button positions
pos_btt1 = [550, 100]
pos_btt2 = [550, 170]
pos_btt3 = [550, 240]

# -------------------------------------------------------------------------
# Init Pygame and initial configurations.
# -------------------------------------------------------------------------

pygame.init()
surface = pygame.display.set_mode((733, 500))
pygame.display.set_caption('Scientific Puzzle')
clock = pygame.time.Clock()
surface.fill(Black)

# Images
bg = pygame.image.load('Background.jpg')
btt = pygame.image.load('Button.jpg')
space = pygame.image.load("game.png")

# -------------------------------------------------------------------------
# Aux methods
# -------------------------------------------------------------------------


def text_objects(text, font):
    text_surface = font.render(text, True, White)
    return text_surface, text_surface.get_rect()


def put_text(text, pos, f_size):
    py_text = pygame.font.Font('freesandbold.ttf', f_size)
    text_surf, text_rect = text_objects(text, py_text)
    surface.blit(text_surf, text_rect)

# -------------------------------------------------------------------------
# Main loop.
# -------------------------------------------------------------------------


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -1
            elif event.key == pygame.K_RIGHT:
                x_change = 1
            elif event.key == pygame.K_UP:
                y_change = -1
            elif event.key == pygame.K_DOWN:
                y_change = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP:
                y_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 0

    surface.blit(bg, [0, 0])

    surface.blit(space, [15, 15])
    surface.blit(space, [15, 15])

    surface.blit(btt, pos_btt1)
    # put_text("Cambiar Modo", btt1, 12)
    surface.blit(btt, pos_btt2)
    surface.blit(btt, pos_btt3)
    pygame.display.update()  # draws the Surface object returned by pygame.display.set_mode() to the screen
    clock.tick(60)  # 30 Frames per second
