from game_config import *
import pygame
import random

class Game:
    #constructor for the game class
    def __init__(self, win, snake):
        #window for the game
        self.win = win
        #Snake object for the game 
        self.snake = snake
        #Generate a fruit at the start of the game
        self.fruit = self.generate_fruit()

    #Function to draw the grid on the game window.
    def draw_grid(self):
        #calculate cell size based on window size and number of columns
        cell_size = WIDTH // COLS
        
        #Draw lines for grid using a for loop in a foor loop
        for i in range(ROWS):
            pygame.draw.line(self.win, WHITE, (0, i * cell_size), (WIDTH, i * cell_size))
            for j in range(COLS):
                pygame.draw.line(self.win, WHITE, (j * cell_size, 0), (j * cell_size, HEIGHT))

    #Function to update the screen with the current game state
    def update_screen(self):
        self.win.fill(BLACK)
        self.draw_grid()
        self.draw_snake()
        self.draw_fruit()
        pygame.display.update()

    #Function to draw the snake on the game window
    def draw_snake(self):
        cell_size = WIDTH // COLS
        for pos in self.snake.get_body():
            pygame.draw.rect(self.win, GREEN, (pos[0]*cell_size, pos[1]*cell_size, cell_size, cell_size))

        #Draw the eyes on the head
        head = self.snake.get_head()
        eye_size = cell_size // 5  # Adjust as needed
        gap = cell_size // 4  # Adjust as needed
        pygame.draw.rect(self.win, WHITE, (head[0]*cell_size + gap, head[1]*cell_size + gap, eye_size, eye_size))
        pygame.draw.rect(self.win, WHITE, (head[0]*cell_size + cell_size - eye_size - gap, head[1]*cell_size + gap, eye_size, eye_size))

    #Draw fruit on the game window
    def draw_fruit(self):
        cell_size = WIDTH // COLS
        pygame.draw.rect(self.win, RED, (self.fruit[0]*cell_size, self.fruit[1]*cell_size, cell_size, cell_size))

    #Function to check if the snake has collided with itself
    def check_collision(self):
        head = self.snake.get_head()
        if head in self.snake.get_body()[1:]:
            return True

    #Function to check if the snake has eaten the fruit
    def check_eat(self):
        if self.snake.get_head() == self.fruit:
            return True
        return False

    #Function to generate a new fruit at a random location not occupied by the snake
    def generate_fruit(self):
        while True:
            pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            if pos not in self.snake.get_body():
                return pos

    #Function to show the score
    def draw_score(self, score):
        font = pygame.font.SysFont(SCORE_FONT, 25)
        text = font.render(f'Score: {score}', 1, WHITE)
        self.win.blit(text, (WIDTH - 100, 10))

    #Handle a loss, player has to press enter to continue
    def draw_game_over(self, score):
        font = pygame.font.SysFont(SCORE_FONT, 40)
        game_over_text = font.render('GG, press ENTER to play again', 1, RED)
        score_text = font.render(f'Score: {score}', 1, RED)
        self.win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        self.win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + game_over_text.get_height()))
        pygame.display.update()
