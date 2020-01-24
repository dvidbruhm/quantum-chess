import pygame
from entity import Entity
from utils import IntVec, get_inverse_color

class Piece(Entity):

    def __init__(self, pos, depth, board_pos, color, image, board):
        Entity.__init__(self, pos, depth)
        self.color = color
        self.image = image
        self.board = board
        self.board_pos = board_pos

        self.pos = IntVec(
            self.board.pos.x + self.board_pos.x * self.board.tile_size,
            self.board.pos.y + self.board_pos.y * self.board.tile_size
        )
        self.is_selected = False

    def get_possible_moves(self):
        raise NotImplementedError

    def update(self, dt):
        if self.is_selected:
            mouse_pos = pygame.mouse.get_pos()
            self.pos.x = mouse_pos[0] - self.board.tile_size/2
            self.pos.y = mouse_pos[1] - self.board.tile_size/2
        else:
            self.pos = IntVec(
                self.board.pos.x + self.board_pos.x * self.board.tile_size,
                self.board.pos.y + self.board_pos.y * self.board.tile_size
            )


    def render(self, screen):
        self.rect = pygame.Rect(
            self.pos.x,
            self.pos.y,
            self.board.tile_size,
            self.board.tile_size
        )
        screen.blit(self.image, self.rect)

    def events(self, event):
        pass

class Pawn(Piece):
    def get_possible_moves(self):
        possible_moves = []

        if self.color == "black":
            direction = 1
        elif self.color == "white":
            direction = -1

        front_pos = IntVec(
            self.board_pos.x,
            self.board_pos.y + direction
        )

        if not self.board.is_occupied(front_pos):
            possible_moves.append(front_pos)
        
        pos1 = IntVec(
            self.board_pos.x + 1,
            self.board_pos.y + direction
        )
        pos2 = IntVec(
            self.board_pos.x - 1,
            self.board_pos.y + direction
        )

        for pos in [pos1, pos2]:
            if self.board.is_occupied(pos) and self.board.get_piece_at(pos).color == get_inverse_color(self.color):
                possible_moves.append(pos)

        return possible_moves

class Knight(Piece):
    def get_possible_moves(self):
        possible_moves = []

        positions = [
            IntVec(1, 2),
            IntVec(1, -2),
            IntVec(-1, 2),
            IntVec(-1, -2),
            IntVec(2, 1),
            IntVec(2, -1),
            IntVec(-2, 1),
            IntVec(-2, -1)
        ]

        for pos in positions:
            dest_pos = self.board_pos + pos
            if self.board.is_pos_on_board(dest_pos):
                if self.board.get_piece_at(dest_pos) and not self.board.get_piece_at(dest_pos).color == self.color:
                    possible_moves.append(dest_pos)
                if not self.board.get_piece_at(dest_pos):
                    possible_moves.append(dest_pos)

        return possible_moves

class Bishop(Piece):
    def get_possible_moves(self):
        pass

class Tower(Piece):
    def get_possible_moves(self):
        pass

class Queen(Piece):
    def get_possible_moves(self):
        pass

class King(Piece):
    def get_possible_moves(self):
        possible_moves = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                dest_pos = self.board_pos + IntVec(i, j)
                if self.board.is_pos_on_board(dest_pos):
                    if self.board.get_piece_at(dest_pos) and not self.board.get_piece_at(dest_pos).color == self.color:
                        possible_moves.append(dest_pos)
                    if not self.board.get_piece_at(dest_pos):
                        possible_moves.append(dest_pos)