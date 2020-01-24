import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("Quantum Chess")

from game import game

game.mainloop()