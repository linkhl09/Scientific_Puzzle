# -------------------------------------------------------------------------
# Developed by:
# Andrés Hernández: linkhl09
# Felipe Parra: Parr0sky
# -------------------------------------------------------------------------
from builtins import bool
from itertools import accumulate

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

# Board init pos
init_pos = np.array([15, 15])

#timer survival
counter, counterText = 30, '30'.rjust(3)
pos_counter=[850,500]
isSurvival=False

#timer adventure
counterUp, counterUpText = 0, '0'.rjust(3)
pos_counter=[850,500]
# Button positions
pos_btt3x3 = [790, 70]
pos_btt4x4 = [850, 70]
pos_btt5x5 = [910, 70]
pos_btt_ma = [800, 170]
pos_btt_md = [800, 230]
pos_btt_s1 = [790, 330]  # Fibonacci.
pos_btt_s2 = [850, 330]  # Quadratic
pos_btt_s3 = [910, 330]  # Primes
pos_btt_s4 = [790, 390]  # Powers of 2
pos_btt_s5 = [850, 390]  # Even Numbers
pos_btt_s6 = [910, 390]  # Odd Numbers

# Text positions
pos_b_s    = [875, 45]
pos_txt3x3 = [815, 95]
pos_txt4x4 = [875, 95]
pos_txt5x5 = [935, 95]

pos_mod    = [875, 150]
pos_txt_ma = [875, 195]
pos_txt_md = [875, 255]

pos_series = [875, 310]
pos_txt_s1 = [815, 355]  # Fibonacci.
pos_txt_s2 = [875, 355]  # Quadratic
pos_txt_s3 = [935, 355]  # Primes
pos_txt_s4 = [815, 415]  # Powers of 2
pos_txt_s5 = [875, 415]  # Even Numbers
pos_txt_s6 = [935, 415]  # Odd Numbers


# Font sizes.
f_size_tit = 28
f_size_btt = 25
f_size_1   = 140
f_size_2   = 120
f_size_3   = 100

# Wood Frame sizes
size_1 = 195
size_2 = 146
size_3 = 117

# -------------------------------------------------------------------------
# World attributes
# -------------------------------------------------------------------------
change = False
board_size = 3
act_size = size_1
act_f_size = f_size_1
world_matrix = [["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"]]


# -------------------------------------------------------------------------
# Init Pygame and initial configurations.
# -------------------------------------------------------------------------

pygame.init()
surface = pygame.display.set_mode((1000, 615))
pygame.display.set_caption('Scientific Puzzle')
clock = pygame.time.Clock()
surface.fill(Black)

# Images
bg = pygame.image.load('Background(or).jpg')
btt = pygame.image.load('Button.jpg')
btt_s = pygame.image.load('Button size.jpg')

space = pygame.image.load("game1.png")
py_text=0
# -------------------------------------------------------------------------
# Aux methods
# -------------------------------------------------------------------------


def text_objects(text, font):
    text_surface = font.render(text, True, White)
    return text_surface, text_surface.get_rect()


def put_text(text, pos, f_size):
    py_text = pygame.font.Font('Roboto-Black.ttf', f_size)
    text_surf, text_rect = text_objects(text, py_text)
    text_rect.center = pos
    surface.blit(text_surf, text_rect)



# -------------------------------------------------------------------------
# Main loop.
# -------------------------------------------------------------------------


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:


            if event.type == pygame.KEYDOWN:
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
    counter -= 0.0625
    counterText = str(int(counter)).rjust(3)+" sec" if counter > 0 else 'boom!'
    counterUp += 0.0625
    counterUpText = str(int(counterUp)).rjust(3) + " sec" if counter > 0 else 'boom!'
    # Set background
    surface.blit(bg, [0, 0])

    # Board
    if change:
        if board_size == 3:
            act_size = size_1
            space = pygame.image.load("game1.png")
            act_f_size = f_size_1
        elif board_size == 5:
            act_size = size_2
            space = pygame.image.load("game2.png")
            act_f_size = f_size_2
        elif board_size == 6:
            act_size = size_3
            space = pygame.image.load("game3.png")
            act_f_size = f_size_3
    for i in range(board_size):
        for j in range(board_size):
            x = init_pos[0] + (i * act_size)
            y = init_pos[1] + (j * act_size)
            act_pos = [x, y]
            surface.blit(space, act_pos)
            put_text(world_matrix[i][j], [x + np.floor(act_size/2), y + np.floor(act_size/2)], act_f_size)


    # Buttons board size
    put_text("Board size", pos_b_s, f_size_tit)
    surface.blit(btt_s, pos_btt3x3)
    put_text("3x3", pos_txt3x3, f_size_btt)
    surface.blit(btt_s, pos_btt4x4)
    put_text("4x4", pos_txt4x4, f_size_btt)
    surface.blit(btt_s, pos_btt5x5)
    put_text("5x5", pos_txt5x5, f_size_btt)

    # Buttons game mode
    put_text("Board size", pos_mod, f_size_tit)
    surface.blit(btt, pos_btt_ma)
    put_text("Adventure", pos_txt_ma, f_size_btt)
    surface.blit(btt, pos_btt_md)
    put_text("Challenge", pos_txt_md, f_size_btt)

    # Buttons series
    put_text("Board size", pos_series, f_size_tit)
    surface.blit(btt_s, pos_btt_s1)
    put_text("Fib", pos_txt_s1, f_size_btt)
    surface.blit(btt_s, pos_btt_s2)
    put_text("X", pos_txt_s2, f_size_btt)
    surface.blit(btt_s, pos_btt_s3)
    put_text("Pri", pos_txt_s3, f_size_btt)
    surface.blit(btt_s, pos_btt_s4)
    put_text("2", pos_txt_s4, f_size_btt)
    surface.blit(btt_s, pos_btt_s5)
    put_text("Even", pos_txt_s5, f_size_btt)
    surface.blit(btt_s, pos_btt_s6)
    put_text("Odd", pos_txt_s6, f_size_btt)

    if isSurvival:
        put_text("Time remaining: ", pos_counter, f_size_tit)
        put_text(counterText, (pos_counter[0], pos_counter[1] + 40), f_size_btt)
    else:
        put_text("Time Elapsed: ", pos_counter, f_size_tit)
        put_text(counterUpText, (pos_counter[0], pos_counter[1] + 40), f_size_btt)
    pygame.display.update()  # draws the Surface object returned by pygame.display.set_mode() to the screen
    clock.tick(60)  # 30 Frames per second
