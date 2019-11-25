# -------------------------------------------------------------------------
# Developed by:
# Andrés Hernández: linkhl09
# Felipe Parra: Parr0sky
# -------------------------------------------------------------------------
from tkinter import W

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

# Timer survival
counter, counterText = 30, '30'.rjust(3)
pos_counter=[850,500]
isSurvival=False

# Timer adventure
counterUp, counterUpText = 0, '0'.rjust(3)
pos_counter=[850,500]

# Button positions
pos_btt3x3 = [790, 70]
pos_btt4x4 = [850, 70]
pos_btt5x5 = [910, 70]
pos_btt_ma = [790, 170]
pos_btt_md = [790, 230]
pos_btt_s1 = [790, 330]  # Fibonacci.
pos_btt_s2 = [850, 330]  # Quadratic
pos_btt_s3 = [910, 330]  # Primes
pos_btt_s4 = [790, 390]  # Powers of 2
pos_btt_s5 = [850, 390]  # Even Numbers
pos_btt_s6 = [910, 390]  # Odd Numbers

# Text positions
pos_b_s    = [875, 45]
pos_mod    = [875, 150]
pos_series = [875, 310]

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
# -------------------------------------------------------------------------
# Aux methods
# -------------------------------------------------------------------------


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def put_text(text, pos, f_size, color):
    py_text = pygame.font.Font('Roboto-Black.ttf', f_size)
    text_surf, text_rect = text_objects(text, py_text, color)
    text_rect.center = pos
    surface.blit(text_surf, text_rect)


def button(msg, texture, pos, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    surface.blit(texture, pos)
    pos_txt = [pos[0]+np.floor(w/2), pos[1]+np.floor(h/2)]
    if pos[0]+w > mouse[0] > pos[0] and pos[1]+h > mouse[1] > pos[1]:
        put_text(msg, pos_txt, f_size_btt, Black)
        if click[0] == 1:  # and action != None:
            # action()
            print("Esto es para la segunda entrega, que pereza")
    else:
        put_text(msg, pos_txt, f_size_btt, White)


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

    # Timer
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
            put_text(world_matrix[i][j], [x + np.floor(act_size/2), y + np.floor(act_size/2)], act_f_size, White)

    # Buttons board size
    put_text("Board size", pos_b_s, f_size_tit, White)
    button("3x3", btt_s, pos_btt3x3, 50, 50)
    button("4x4", btt_s, pos_btt4x4, 50, 50)
    button("5x5", btt_s, pos_btt5x5, 50, 50)

    # Buttons game mode
    put_text("Game mode", pos_mod, f_size_tit, White)
    button("Adventure", btt, pos_btt_ma, 170, 50)
    button("Challenge", btt, pos_btt_md, 170, 50)

    # Buttons series
    put_text("Board size", pos_series, f_size_tit, White)
    button("Fib", btt_s, pos_btt_s1, 50, 50)
    button("X^2", btt_s, pos_btt_s2, 50, 50)
    button("Pri", btt_s, pos_btt_s3, 50, 50)
    button("2^n", btt_s, pos_btt_s4, 50, 50)
    button("Even", btt_s, pos_btt_s5, 50, 50)
    button("Odd", btt_s, pos_btt_s6, 50, 50)

    # Timer txt
    if isSurvival:
        put_text("Time remaining: ", pos_counter, f_size_tit, White)
        put_text(counterText, (pos_counter[0], pos_counter[1] + 40), f_size_btt, White)
    else:
        put_text("Time Elapsed: ", pos_counter, f_size_tit, White)
        put_text(counterUpText, (pos_counter[0], pos_counter[1] + 40), f_size_btt, White)
    pygame.display.update()  # draws the Surface object returned by pygame.display.set_mode() to the screen
    clock.tick(60)  # 30 Frames per second
