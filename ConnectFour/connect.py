
import pygame       #Pygame for GUI
import sys          #Sys to control system-specific parameters and functions
import math         #Math for math functions

#Defining colors in RGB format
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

#Defining board dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7

#Function to create the intial game board using numpy. The board is a 2D array filled with zeroes.
#Zero represents empty space.






#Function to get the lowest open row in chosen column. Takes the column the player chooses on the board.
# It goes through each row of the column and returns the first empty row in it.


#Function to draw the game board. It prints rectangles for the board and circles for the pieces.
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))    
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)      
    pygame.display.update()

#Creates game board by calling the create_board function.
board = create_board()
print_board()
game_over = False
turn = 0

#Initializes the pygame library.
pygame.init()

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
#Radius of the pieces.
RADIUS = int(SQUARESIZE/2 - 5)


screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("Monospace", 75)

#The main game loop.
while not game_over:
    #Checks for events(mose movement, game close, mouse click)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            #print(event.pos)
            #Ask player 1 for input
            if turn == 0:
                posx = event.pos[0]
                #Calculate the column where the piece will be dropped.
                col = int(math.floor(posx/SQUARESIZE))
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

            # #Ask for player 2 input
            else:
                posy = event.pos[0]
                col = int(int(math.floor(posy/SQUARESIZE)))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins", 2, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True

            
            if is_tie(board):
                label = myfont.render("It's a tie!", 1, (255,255,255))
                screen.blit(label, (40,10))
                game_over = True


            print_board()
            draw_board(board)
            turn += 1
            turn = turn % 2

if game_over:
    pygame.time.wait(2000)