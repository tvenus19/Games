#Defining colors in RGB format
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

#Defining board dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7

#Squaresize represents the size of each square in the game gird. Value in pixels.
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)

#Defining size of font used in pygame display
FONT_SIZE = 75
