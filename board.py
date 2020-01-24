import pygame

from entity_manager import entity_manager
from entity import Entity
from piece import Piece
from utils import IntVec, get_inverse_color
from messager import messager

class Board(Entity):

    def __init__(self, pos: IntVec, depth: int, size: IntVec, tile_size: int, color_black, color_white):
        Entity.__init__(self, pos, depth)
        self.size = size
        self.tile_size = tile_size
        self.black = color_black
        self.white = color_white

        self.pieces = []
        self.dead_pieces = []
        self.selected_piece = None
        # list of positions to highlight
        self.highlighted_tiles = []
        self.click = False
        self.click_pos = None
        self.color_turn = "white"

        self.pixel_size = self.size * self.tile_size
    
    def update(self, dt):
        if self.click:
            for piece in self.get_pieces_of_color(self.color_turn):
                board_click_pos = self.get_click_pos(self.click_pos)
                
                if not piece.is_selected and piece.rect.collidepoint(self.click_pos) and not self.selected_piece:
                    piece.is_selected = True
                    self.selected_piece = piece
                    self.highlight_tiles(piece.get_possible_moves())

                elif piece.is_selected and board_click_pos is not None:
                    piece.is_selected = False
                    self.selected_piece = None

                    if board_click_pos in piece.get_possible_moves():

                        if not board_click_pos == piece.board_pos:
                            # piece moved, change turn
                            self.change_turn()
                        
                        piece_at_location = self.get_piece_at(board_click_pos)
                        piece.board_pos = board_click_pos
                        if piece_at_location and piece_at_location.color != piece.color:
                            self.add_dead_piece(piece_at_location)
                            print(piece_at_location.color + " " + piece_at_location.__class__.__name__ + " devoured at " + str(piece_at_location.board_pos.to_tuple()) + ".")
                            

                    self.clear_highlight()
                    break

            self.click = False
            self.click_pos = None
    
    def render(self, screen):
        for i in range(self.size):
            for j in range(self.size):
                rect = (i * self.tile_size + self.pos.x, j * self.tile_size + self.pos.y, self.tile_size, self.tile_size)
                color = self.white if ((i + j) % 2) == 0 else self.black
                pygame.draw.rect(screen, color, rect)

                if IntVec(i, j) in self.highlighted_tiles:

                    pygame.draw.circle(
                        screen, 
                        (0,255,0) if not self.get_piece_at(IntVec(i, j)) else (255,0,0), 
                        (rect[0] + int(self.tile_size/2), rect[1] + int(self.tile_size/2)), 
                        20
                    )

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            self.click = True
            self.click_pos = mouse_pos            
    
    def highlight_tiles(self, tiles):
        self.highlighted_tiles = tiles
    
    def clear_highlight(self):
        self.highlighted_tiles = []
    
    def add_piece(self, piece: Piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)

    def add_dead_piece(self, piece):
        self.remove_piece(piece)
        self.dead_pieces.append(piece)
        entity_manager.remove(piece)
    
    def get_piece_at(self, pos: IntVec):
        for piece in self.pieces:
            if piece.board_pos == pos:
                return piece
        return None

    def is_occupied(self, pos: IntVec):
        for piece in self.pieces:
            if piece.board_pos == pos:
                return True
        return False
    
    def is_click_on_board(self, mouse_pos):
        return pygame.Rect(self.pos.to_tuple(), (self.pixel_size, self.pixel_size)).collidepoint(mouse_pos)
    
    def is_pos_on_board(self, pos: IntVec):
        if pos.x < 0 or pos.x > self.size or pos.y < 0 or pos.y > self.size:
            return False
        return True

    def get_click_pos(self, mouse_pos):
        if not self.is_click_on_board(mouse_pos):
            return None
        
        click_pos = IntVec(
            int((mouse_pos[0] - self.pos.x) / self.tile_size),
            int((mouse_pos[1] - self.pos.y) / self.tile_size)
        )

        return click_pos
    
    def get_pieces_of_color(self, color):
        return filter(lambda x: x.color == color, self.pieces)

    def change_turn(self):
        self.color_turn = get_inverse_color(self.color_turn)
        messager.set_message(self.color_turn + "'s turn")
        