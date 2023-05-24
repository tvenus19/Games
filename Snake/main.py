from game_config import WIDTH, HEIGHT, ROWS, COLS, SNAKE_SPEED
from game_utils import Game
from snake import Snake
from event_handler import handle_events
import pygame
import sys

#Function to wait for user input (pressing enter)
def wait_for_key():
    while True:
        for event in pygame.event.get():
            #Quite the game if the quit even is triggered
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Break the loop if enter is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
#Main function to run the game
def main():
    pygame.init()
    #Set up the game window
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    #Set the window title
    pygame.display.set_caption('Snake Game')

    # Define start position in cells
    start_pos = (ROWS // 2, COLS // 2)
    #Create a new snake object
    snake = Snake(start_pos)
    #Crate a new game object
    game = Game(win, snake)

    #Create a clock object to control the game speed
    clock = pygame.time.Clock()
    score = 0

    while True:
        #Limit the speed of the game to SNAKE_SPEED
        clock.tick(SNAKE_SPEED)

        #Handle user input
        handle_events(snake)
        
        #If a collision happened, draw the game over screen, wait for enter.
        #Reset the snake position and the score
        if game.check_collision():
            game.draw_game_over(score)
            wait_for_key()
            snake.reset(start_pos)
            score = 0

        #If teh snake eat a fruit, make the snake grow, update the score and generate a new fruit.
        if game.check_eat():
            snake.grow()
            score += 1
            game.fruit = game.generate_fruit()

        snake.move()

        #Update the screen with the current game state
        game.update_screen()
        game.draw_score(score)
        #Update the display
        pygame.display.update()

if __name__ == "__main__":
    main()
