# -------------------------------------------------------------------------
# Developed by:
# Andrés Hernández: linkhl09
# Felipe Parra: Parr0sky
# -------------------------------------------------------------------------
from tkinter import W

import numpy as np
import pygame
import sys
import math as m
from pygame.locals import *

# -------------------------------------------------------------------------
# Logic
# -------------------------------------------------------------------------


class World:
    size = 3
    serie = 1
    number = size**2
    matrix = np.zeros((size, size))

    #1:Fib, 2: X^2, 3: Primes, 4: 2^n, 5: Even, 6: Odd
    def __init__(self, size, serie):
        self.size = size
        self.serie = serie
        self.number=size**2
        self.matrix = np.zeros((size, size))

    def fib(self, lim):
        arr=np.zeros(lim)
        cont=0
        while cont<lim:
            if cont<=1:
                arr[cont]=1
            else:
                arr[cont]= arr[cont-1]+arr[cont-2]
            cont+=1
        return arr

    def square(self, lim):
        arr=np.zeros(lim)
        cont=0
        while cont<lim:
            arr[cont]=cont**2
            cont+=1
        return arr

    def p3(self, num):
        i = 2
        primo = True
        # Reviso y si el modulo del número con algún otro número es 0, es porque no es primo.
        while primo and i < num:
            if m.fmod(num, i) == 0:
                primo = False
            i = i + 1
        return primo

    def primes(self,lim):
        arr=np.zeros(lim)
        cont=0
        i = 0
        while cont<lim:
            if self.p3(i) and i!=0 and i!=1:
                arr[cont]=i
                cont+=1
            i+=1
        return arr

    def quadratic(self,lim):
        arr = np.zeros(lim)
        cont = 0
        while cont < lim:
            arr[cont] = 2**cont
            cont+=1
        return arr

    def even(self, lim):
        arr = np.zeros(lim)
        cont = 0
        i = 0
        while cont < lim:
            if i==0:
                arr[cont]=i
                cont+=1
            elif m.fmod(i,2)==0:
                arr[cont] = i
                cont += 1
            i += 1

        return arr

    def odd(self, lim):
        arr = np.zeros(lim)
        cont = 0
        i = 0
        while cont < lim:
            if m.fmod(i,2)==1:
                arr[cont] = i
                cont += 1
        i += 1

        return arr

    def get_matrix(self):
        return np.array2string(self.matrix)

    def initialize(self):
        if self.serie==1:
            arr=self.fib(self.number)
            cont=0
            for i in range(0,np.size(self.matrix,axis=1)):
                for j in range(0,np.size(self.matrix,axis=1)):
                    self.matrix[i,j]=int(arr[cont])
                    cont+=1
        elif self.serie==2:
            arr=self.square(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    cont += 1
        elif self.serie==3:
            arr=self.primes(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    cont += 1
        elif self.serie==4:
            arr=self.quadratic(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    cont += 1
        elif self.serie==5:
            arr = self.even(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    cont += 1
        elif self.serie==6:
            arr = self.odd( self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    cont += 1


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
pos_counter = [850, 500]
is_challenge = False

# Timer adventure
counterUp, counterUpText = 0, '0'.rjust(3)

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
board_size = 3
act_size = size_1
act_f_size = f_size_1
w = World(board_size, 1)
w.initialize()
# world_matrix = Aquí yace el honor de Andres.


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
        if click[0] == 1 and action != None:
            if msg.startswith("3"):
                action(3)
            elif msg.startswith("4"):
                action(4)
            elif msg.startswith("5"):
                action(5)
            else:
                action()
    else:
        put_text(msg, pos_txt, f_size_btt, White)


def size_change(new_size):
    global board_size
    global act_size
    global space
    global act_f_size
    global world_matrix
    board_size = new_size

    if board_size == 3:
        act_size = size_1
        space = pygame.image.load("game1.png")
        act_f_size = f_size_1
    elif board_size == 4:
        act_size = size_2
        space = pygame.image.load("game2.png")
        act_f_size = f_size_2
        world_matrix = [["1", "4", "7", "e"], ["2", "5", "8", "i"], ["3", "6", "9", "o"], ["u", "a", "k", "p"]]
    elif board_size == 5:
        act_size = size_3
        space = pygame.image.load("game3.png")
        act_f_size = f_size_3
        world_matrix = [["1", "4", "7", "e", "4"], ["1", "4", "7", "e", "4"], ["1", "4", "7", "e", "4"], ["1", "4", "7", "e", "4"], ["1", "4", "7", "e", "4"]]


def set_challenge():
    global is_challenge
    is_challenge = True


def set_adventure():
    global is_challenge
    is_challenge = False


def fib():
    print("Llamar al mundo, s1")


def square():
    print("Llamar al mundo, s2")


def pri():
    print("Llamar al mundo, s3")


def quad():
    print("Llamar al mundo, s4")


def even():
    print("Llamar al mundo, s5")


def odd():
    print("Llamar al mundo, s6")


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
    for i in range(board_size):
        for j in range(board_size):
            x = init_pos[0] + (i * act_size)
            y = init_pos[1] + (j * act_size)
            act_pos = [x, y]
            surface.blit(space, act_pos)
            put_text(world_matrix[i][j], [x + np.floor(act_size/2), y + np.floor(act_size/2)], act_f_size, White)

    # Buttons board size
    put_text("Board size", pos_b_s, f_size_tit, White)
    button("3x3", btt_s, pos_btt3x3, 50, 50, size_change)
    button("4x4", btt_s, pos_btt4x4, 50, 50, size_change)
    button("5x5", btt_s, pos_btt5x5, 50, 50, size_change)

    # Buttons game mode
    put_text("Game mode", pos_mod, f_size_tit, White)
    button("Adventure", btt, pos_btt_ma, 170, 50, set_challenge)
    button("Challenge", btt, pos_btt_md, 170, 50, set_adventure)

    # Buttons series
    put_text("Board size", pos_series, f_size_tit, White)
    button("Fib", btt_s, pos_btt_s1, 50, 50, fib)
    button("X^2", btt_s, pos_btt_s2, 50, 50, square)
    button("Pri", btt_s, pos_btt_s3, 50, 50, pri)
    button("2^n", btt_s, pos_btt_s4, 50, 50, quad)
    button("Even", btt_s, pos_btt_s5, 50, 50, even)
    button("Odd", btt_s, pos_btt_s6, 50, 50, odd)

    # Timer txt
    if is_challenge:
        put_text("Time remaining: ", pos_counter, f_size_tit, White)
        put_text(counterText, (pos_counter[0], pos_counter[1] + 40), f_size_btt, White)
    else:
        put_text("Time Elapsed: ", pos_counter, f_size_tit, White)
        put_text(counterUpText, (pos_counter[0], pos_counter[1] + 40), f_size_btt, White)
    pygame.display.update()  # draws the Surface object returned by pygame.display.set_mode() to the screen
    clock.tick(60)  # 30 Frames per second
