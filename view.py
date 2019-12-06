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


# Object used to manage the logic of the program.
class World:
    size = 3
    series = 1
    number = size**2
    matrix = np.zeros((size, size))
    strMatrix = 0
    initial = [np.size(matrix, axis=1)-1,np.size(matrix, axis=1)-1]
    # Constructor of the class.
    # size: The size of the square matrix.
    # series: The series wanted. This are the possible values:
    #         1:Fib, 2: X^2, 3: Primes, 4: 2^n, 5: Even, 6: Odd
    def __init__(self, size, series):
        self.size = size
        self.series = series
        self.number = size**2
        self.matrix = np.zeros((size, size))
        if size == 5:
            self.strMatrix = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""],["", "", "", "", ""]]
        elif size == 4:
            self.strMatrix = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
        elif size == 3:
            self.strMatrix = [["", "", ""], ["", "", ""], ["", "", ""]]

    # Calculates fibonacci till certain number of iterations.
    # lim: The number of iterations.
    def fib(self, lim):
        arr = np.zeros(lim)
        cont = 0
        while cont < lim:
            if cont <= 1:
                arr[cont] = 1
            else:
                arr[cont] = arr[cont-1]+arr[cont-2]
            cont += 1
        return arr

    # Calculates the square series (x^2) till certain number of iterations.
    # lim: The number of iterations.
    def square(self, lim):
        arr = np.zeros(lim)
        cont = 0
        while cont < lim:
            arr[cont] = cont**2
            cont += 1
        return arr

    # Check if a number is prime using the definition.
    def is_prime(self, num):
        i = 2
        primo = True
        # Reviso y si el modulo del número con algún otro número es 0, es porque no es primo.
        while primo and i < num:
            if m.fmod(num, i) == 0:
                primo = False
            i = i + 1
        return primo

    # Calculates the prime number series till certain number of iterations.
    # lim: The number of iterations.
    def primes(self, lim):
        arr = np.zeros(lim)
        cont = 0
        i = 0
        while cont < lim:
            if self.is_prime(i) and i != 0 and i != 1:
                arr[cont] = i
                cont += 1
            i += 1
        return arr

    # Calculates the quadratic series (2^x) till certain number of iterations.
    # lim: The number of iterations.
    def quadratic(self, lim):
        arr = np.zeros(lim)
        cont = 0
        while cont < lim:
            arr[cont] = 2**cont
            cont += 1
        return arr

    # Calculates the even number series till certain number of iterations.
    # lim: The number of iterations.
    def even(self, lim):
        arr = np.zeros(lim)
        cont = 0
        i = 0
        while cont < lim:
            if i == 0:
                arr[cont] = i
                cont += 1
            elif m.fmod(i, 2) == 0:
                arr[cont] = i
                cont += 1
            i += 1

        return arr

    # Calculates the odd number series till certain number of iterations.
    # lim: The number of iterations.
    def odd(self, lim):
        arr = np.zeros(lim)
        cont = 0
        i = 0
        while cont < lim:
            if m.fmod(i, 2) == 1:
                arr[cont] = i
                cont += 1
            i += 1

        return arr

    # Gets the matrix as an string.
    def get_matrix(self):
        return np.array2string(self.matrix)

    # Move -1 to specified direction
    def move(self, dir):

        # 1 means down
        if dir == 1 and self.initial[0]+1 < np.size(self.matrix, axis=1):

            self.matrix[self.initial[0],self.initial[1]] = self.matrix[self.initial[0]+1,self.initial[1]]
            self.strMatrix[self.initial[0]][self.initial[1]] = self.strMatrix[self.initial[0]+1][self.initial[1]]
            self.initial[0] = self.initial[0] + 1
            self.matrix[self.initial[0], self.initial[1]]=-1
            self.strMatrix[self.initial[0]][self.initial[1]] = ""
        # 2 means up
        elif dir == 2 and self.initial[0]-1 >= 0:
            self.matrix[self.initial[0], self.initial[1]] = self.matrix[self.initial[0] - 1, self.initial[1]]
            self.strMatrix[self.initial[0]][self.initial[1]] = self.strMatrix[self.initial[0] - 1][self.initial[1]]
            self.initial[0] = self.initial[0] - 1
            self.matrix[self.initial[0], self.initial[1]] = -1
            self.strMatrix[self.initial[0]][self.initial[1]] = ""
        # 3 means left
        elif dir == 3 and self.initial[1]-1 >= 0:
            self.matrix[self.initial[0], self.initial[1]] = self.matrix[self.initial[0], self.initial[1]-1]
            self.strMatrix[self.initial[0]][self.initial[1]] = self.strMatrix[self.initial[0]][self.initial[1] -1]
            self.initial[1] = self.initial[1] - 1
            self.matrix[self.initial[0], self.initial[1]] = -1
            self.strMatrix[self.initial[0]][self.initial[1]] = ""
        # 4 means right
        elif dir == 4 and self.initial[1]+1 < np.size(self.matrix, axis=1):
            self.matrix[self.initial[0], self.initial[1]] = self.matrix[self.initial[0], self.initial[1] + 1]
            self.strMatrix[self.initial[0]][self.initial[1]] = self.strMatrix[self.initial[0]][self.initial[1] + 1]
            self.initial[1] = self.initial[1] + 1
            self.matrix[self.initial[0], self.initial[1]] = -1
            self.strMatrix[self.initial[0]][self.initial[1]] = ""
    # Initialize the matrix depending on the series and the size.
    def initialize(self):
        # Fibonacci series.
        if self.series == 1:
            arr = self.fib(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    self.strMatrix[i][j] = str(int(self.matrix[i, j]))
                    cont += 1
        # Square (X^2) series
        elif self.series == 2:
            arr = self.square(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    self.strMatrix[i][j] = str(int(self.matrix[i, j]))
                    cont += 1
        # Prime number series
        elif self.series == 3:
            arr = self.primes(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    self.strMatrix[i][j] = str(int(self.matrix[i, j]))
                    cont += 1
        # Quadratic series
        elif self.series == 4:
            arr = self.quadratic(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    self.strMatrix[i][j] = str(int(self.matrix[i, j]))
                    cont += 1
        # Even number series
        elif self.series == 5:
            arr = self.even(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    self.strMatrix[i][j] = str(int(self.matrix[i, j]))
                    cont += 1
        # Odd number series
        elif self.series == 6:
            arr = self.odd(self.number)
            cont = 0
            for i in range(0, np.size(self.matrix, axis=1)):
                for j in range(0, np.size(self.matrix, axis=1)):
                    self.matrix[i, j] = int(arr[cont])
                    self.strMatrix[i][j] = str(int(self.matrix[i, j]))
                    cont += 1
        self.matrix[self.initial[0], self.initial[1]] = -1
        self.strMatrix[self.initial[0]] [self.initial[1]] = ""


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
pos_btt_am = [790, 170]  # Adventure mode
pos_btt_cm = [790, 230]  # Challenge mode
pos_btt_s1 = [790, 330]  # Fibonacci
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
f_size_1   = 80
f_size_2   = 40
f_size_3   = 20

# Wood Frame sizes
size_1 = 195
size_2 = 146
size_3 = 117

# -------------------------------------------------------------------------
# Interface attributes
# -------------------------------------------------------------------------
board_size = 3
act_size = size_1
act_f_size = f_size_1
w = World(board_size, 1)
w.initialize()

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


# Defines the text surface and the text rect from the given parameters.
# text: The text.
# font: Pygame font for the text.
# color: CONSTRAINT with the color of the text in RGB
def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


# Puts a text in the given position.
# text: The text.
# pos: Position in pixels.
# f_size: Font size to be used.
# color: Color of the text.
def put_text(text, pos, f_size, color):
    py_text = pygame.font.Font('Roboto-Black.ttf', f_size)
    text_surf, text_rect = text_objects(text, py_text, color)
    text_rect.center = pos
    surface.blit(text_surf, text_rect)


# Puts a button with the given texture and message in the interface.
# msg: msg of the button.
# texture: texture of the button. Must be an image.
# pos: Position in pixels.
# width: width of the button.
# h: Height of the button.
# param: Parameter needed for the button function if it has one.
def button(msg, texture, pos, width, h, param, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    surface.blit(texture, pos)
    pos_txt = [pos[0] + np.floor(width / 2), pos[1] + np.floor(h / 2)]
    if pos[0]+width > mouse[0] > pos[0] and pos[1]+h > mouse[1] > pos[1]:
        put_text(msg, pos_txt, f_size_btt, Black)
        if click[0] == 1 and action != None:
            action(param)
    else:
        put_text(msg, pos_txt, f_size_btt, White)


# Changes the size of the board to the size given by parameter. Also changes the images and the actual size of the text
# in the board.
# new_size: new size of the board.
def size_change(new_size):
    global board_size
    global act_size
    global space
    global act_f_size
    global w

    board_size = new_size
    # If we change the board, we are creating a new game, thus, a new world.
    w = World(board_size, 1)
    w.initialize()
    # Update the interface objects.
    if board_size == 3:
        act_size = size_1
        space = pygame.image.load("game1.png")
        act_f_size = f_size_1
    elif board_size == 4:
        act_size = size_2
        space = pygame.image.load("game2.png")
        act_f_size = f_size_2
    elif board_size == 5:
        act_size = size_3
        space = pygame.image.load("game3.png")
        act_f_size = f_size_3


# Sets the actual mode of the game.
# mode: the new mode of the game. True if it's challenge, false instead.
def set_mode(mode):
    global is_challenge
    global counterText
    global counter
    global counterUp
    global counterUpText
    is_challenge = mode
    counterText = '30'.rjust(3)
    counter = 30
    counterUp = 0
    counterUpText = '0'.rjust(3)


# Changes the actual series in the board.
# num: The number of the series wanted. This are the possible values:
#      1:Fib, 2: X^2, 3: Primes, 4: 2^n, 5: Even, 6: Odd
def change_series(num):
    global w
    global act_f_size
    w = World(board_size, num)
    w.initialize()


# -------------------------------------------------------------------------
# Main loop.
# -------------------------------------------------------------------------


while True:
    for event in pygame.event.get():
        # Exit the game.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Keyboard events.
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    w.move(4)
                elif event.key == pygame.K_RIGHT:
                    w.move(3)
                elif event.key == pygame.K_UP:
                    w.move(1)
                elif event.key == pygame.K_DOWN:
                    w.move(2)
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

    # Draws the Board
    for i in range(board_size):
        for j in range(board_size):
            x = init_pos[0] + (i * act_size)
            y = init_pos[1] + (j * act_size)
            act_pos = [x, y]
            surface.blit(space, act_pos)
            put_text(w.strMatrix[j][i], [x + np.floor(act_size / 2), y + np.floor(act_size / 2)], act_f_size, White)

    # Buttons board size
    put_text("Board size", pos_b_s, f_size_tit, White)
    button("3x3", btt_s, pos_btt3x3, 50, 50, 3, size_change)
    button("4x4", btt_s, pos_btt4x4, 50, 50, 4, size_change)
    button("5x5", btt_s, pos_btt5x5, 50, 50, 5, size_change)

    # Buttons game mode
    put_text("Game mode", pos_mod, f_size_tit, White)
    button("Adventure", btt, pos_btt_am, 170, 50, 0, set_mode)
    button("Challenge", btt, pos_btt_cm, 170, 50, 1, set_mode)

    # Buttons series
    put_text("Series", pos_series, f_size_tit, White)
    button("Fib", btt_s, pos_btt_s1, 50, 50, 1, change_series)
    button("X^2", btt_s, pos_btt_s2, 50, 50, 2, change_series)
    button("Pri", btt_s, pos_btt_s3, 50, 50, 3, change_series)
    button("2^n", btt_s, pos_btt_s4, 50, 50, 4, change_series)
    button("Even", btt_s, pos_btt_s5, 50, 50, 5, change_series)
    button("Odd", btt_s, pos_btt_s6, 50, 50, 6, change_series)

    # Timer txt
    if is_challenge:
        put_text("Time remaining: ", pos_counter, f_size_tit, White)
        put_text(counterText, (pos_counter[0], pos_counter[1] + 40), f_size_btt, White)
    else:
        put_text("Time Elapsed: ", pos_counter, f_size_tit, White)
        put_text(counterUpText, (pos_counter[0], pos_counter[1] + 40), f_size_btt, White)
    pygame.display.update()  # draws the Surface object returned by pygame.display.set_mode() to the screen
    clock.tick(60)  # 30 Frames per second
