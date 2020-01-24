import pygame

from entity_manager import entity_manager
from entity import Entity
from config import WIDTH, HEIGHT, WHITE
from utils import IntVec

class Messager(Entity):
    
    def __init__(self, pos, depth, color):
        Entity.__init__(self, pos, depth)
        self.message = "Welcome!"
        self.myfont = pygame.font.SysFont('Comic Sans MS', 40)
        self.color = color

    # TODO add timer?
    def set_message(self, message):
        self.message = message
    
    def render(self, screen):
        surface = self.myfont.render(self.message, False, self.color)
        text_rect = surface.get_rect(center=self.pos.to_tuple())
        screen.blit(surface, text_rect)

messager = Messager(IntVec(WIDTH/2, 50), 0, WHITE)
entity_manager.add(messager)