
##
import numpy as np

import pygame, sys          # import statement that imports the pygame and sys modules
from pygame.locals import *

pygame.init()   # Inicializa cada módulo importado con pygame. it needs to be called first in order for many Pygame functions to work
DISPLAYSURF = pygame.display.set_mode((400, 300))   # Tamaño en pixeles de la superficie de la ventana, tupla: (ancho,alto)
pygame.display.set_caption('Nicolás!')

# RGB Values
Aqua = ( 0, 255, 255)
Black = ( 0, 0, 0)
Blue = ( 0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = (0,128,0)
Lime = ( 0,255, 0)
Maroon = (128, 0, 0)
Navy_Blue = ( 0, 0,128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = ( 0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)

DISPLAYSURF.fill(Navy_Blue)         # Método para llenar de color blanco la superficie del objeto. Método de: pygame.Surface objects

'''
Instrucciones para dibujar diferentes figuras geométricas
'''
# pygame.draw.polygon(surface, color, pointlist, width)
# pygame.draw.line(surface, color, start_point, end_point, width)
# pygame.draw.lines(surface, color, closed, pointlist, width)
# pygame.draw.circle(surface, color, center_point, radius, width)
# pygame.draw.ellipse(surface, color, bounding_rectangle, width)
# pygame.draw.rect(surface, color, rectangle_tuple, width)

pygame.draw.polygon(DISPLAYSURF, Yellow, ((146,0), (291,105),(236,277),(45,105)))
pygame.draw.line(DISPLAYSURF,Teal,(40,40),(120,60),8)
pygame.draw.circle(DISPLAYSURF, Lime, (250,80),50,2)


# Creando la ventana
while True: # Importante: main game loop

    for event in pygame.event.get():    # Módulo event
        if event.type == QUIT:  # Cuando se le da click a la X en la ventana para salir
            pygame.quit()       # Desactiva la librería Pygame
            sys.exit()          # Se encarga de terminar el programa.
    pygame.display.update() # draws the Surface object returned by pygame.display.set_mode() to the screen
