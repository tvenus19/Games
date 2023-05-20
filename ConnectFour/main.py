from game_logic import Game
from game_interface import GameInterface
from game_constants import *

def main():
    #Creates game board by calling the create_board function.
    game = Game(ROW_COUNT, COLUMN_COUNT)

    #Initializes the pygame library.
    pygame.init()

    game_interface = GameInterface(game, SQUARESIZE, RADIUS, FONT_SIZE)

    game_over = False
    turn = 0

    #The main game loop.
    while not game_over:
        #Checks for events(mose movement, game close, mouse click)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                posx = event.pos[0]
                game_interface.handle_mouse_motion(posx, turn)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos[0]
                col = int(math.floor(pos/SQUARESIZE))
                
                if game.is_valid_location(col):
                    row = game.get_next_open_row(col)
                    game.drop_piece(row, col, turn+1)

                    if game.winning_move(turn+1):
                        game_interface.render_win_message(turn+1)
                        game_over = True

                if game.is_tie():
                    game_interface.render_tie_message()
                    game_over = True

                game_interface.draw_board()
                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(2000)

if __name__ == "__main__":
    main()
