import os
import pygame

class AssetManager:

    def __init__(self):
        pass
    
    def load_images(self):
        self.white_pawn = pygame.image.load(os.path.join("assets", "white_pawn.png")).convert_alpha()
        self.black_pawn = pygame.image.load(os.path.join("assets", "black_pawn.png")).convert_alpha()
        self.black_knight = pygame.image.load(os.path.join("assets", "black_knight.png")).convert_alpha()
        self.white_knight = pygame.image.load(os.path.join("assets", "white_knight.png")).convert_alpha()

asset_manager = AssetManager()