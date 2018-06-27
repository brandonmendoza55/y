import sys, pygame
from pygame.locals import*
ALTURA = 300
ANCHO = 300


def main():
	pygame.init()	
	screen = pygame.display.set_mode((ALTURA,ANCHO))
	pygame.display.set_caption("welcome to pygame")
