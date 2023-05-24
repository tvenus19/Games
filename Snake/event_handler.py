from game_config import UP, DOWN, LEFT, RIGHT
import pygame
import sys

#Define a function to handle various events during the game
def handle_events(snake):
    #Loop through all the events
    for event in pygame.event.get():

        #If users closes window, exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Events to happen if a key is pressed.
        #Based on key pressed, change direction of the snake.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT