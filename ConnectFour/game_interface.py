import pygame
from game_constants import *

class GameInterface:
    def __init__(self, screen):
        self.screen = screen
        self.myfont = pygame.font.SysFont("Monospace", FONT_SIZE)

    def draw_board(self, board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))    
                pygame.draw.circle(self.screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(self.screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)      
        pygame.display.update()

    def draw_winning_message(self, winner):
        if winner == 1:
            label = self.myfont.render("Player 1 wins", 1, RED)
        else:
            label = self.myfont.render("Player 2 wins", 1, YELLOW)
        self.screen.blit(label, (40,10))
        pygame.display.update()

    def draw_tie_message(self):
        label = self.myfont.render("It's a tie!", 1, (255,255,255))
        self.screen.blit(label, (40,10))
        pygame.display.update()

    def draw_piece(self, turn, pos):
        pygame.draw.rect(self.screen, BLACK, (0,0, width, SQUARESIZE))
        if turn == 0:
            pygame.draw.circle(self.screen, RED, (pos, int(SQUARESIZE/2)), RADIUS)
        else:
            pygame.draw.circle(self.screen, YELLOW, (pos, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
