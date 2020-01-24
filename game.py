import pygame

from entity_manager import entity_manager
from asset_manager import asset_manager
from config import WIDTH, HEIGHT, FPS, BLACK, WHITE, TILE_SIZE, BOARD_POS, BOARD_SIZE
from utils import IntVec
from messager import messager

from board import Board
from piece import Pawn, Knight


class Game:
    """
    Class that handles the main game loop
    """
    def __init__(self):
        self.quit = False
        
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()

        asset_manager.load_images()

        self.init_game()

    def init_game(self):
        board = Board(IntVec(BOARD_POS[0], BOARD_POS[1]), 1, BOARD_SIZE, TILE_SIZE, BLACK, WHITE)
        entity_manager.add(board)
        

        pawn = Pawn(IntVec(0, 0), 0, IntVec(2, 2), "black", asset_manager.black_pawn, board)
        entity_manager.add(pawn)
        board.add_piece(pawn)

        pawn = Pawn(IntVec(0, 0), 0, IntVec(2, 5), "white", asset_manager.white_pawn, board)
        entity_manager.add(pawn)
        board.add_piece(pawn)

        pawn = Pawn(IntVec(0, 0), 0, IntVec(3, 5), "white", asset_manager.white_pawn, board)
        entity_manager.add(pawn)
        board.add_piece(pawn)

        knight = Knight(IntVec(0, 0), 0, IntVec(4, 5), "white", asset_manager.white_knight, board)
        entity_manager.add(knight)
        board.add_piece(knight)

        entity_manager.sort()
        messager.set_message("White's turn")

    def update(self):
        dt = self.clock.tick(FPS)

        for entity in entity_manager.entities:
            entity.update(dt)

    def render(self):
        self.screen.fill((0, 0, 0))

        for entity in entity_manager.entities:
            entity.render(self.screen)

        pygame.display.flip()

    def events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.quit = True
                break

            for entity in entity_manager.entities:
                entity.events(event)

    def mainloop(self):
        while not self.quit:
            self.update()
            self.render()
            self.events()

game = Game()
