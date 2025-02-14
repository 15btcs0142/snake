import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game Window Size
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Feed Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# Snake Block Size
BLOCK_SIZE = 10
SNAKE_SPEED = 15

# Font
font = pygame.font.SysFont("bahnschrift", 25)

# Game Over Message
def message(msg, color, x, y):
    mesg = font.render(msg, True, color)
    win.blit(mesg, [x, y])

# Game Loop
def gameLoop():
    game_over = False
    game_close = False
    
    x, y = WIDTH//2, HEIGHT//2
    dx, dy = 0, 0
    
    snake_list = []
    length_of_snake = 1
    
    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close:
            win.fill(WHITE)
            message("You Lost! Press Q-Quit or C-Play Again", RED, WIDTH//6, HEIGHT//3)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = BLOCK_SIZE
        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        x += dx
        y += dy
        win.fill(BLUE)
        pygame.draw.rect(win, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        
        for segment in snake_list:
            pygame.draw.rect(win, BLACK, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])
        
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            length_of_snake += 1
        
        clock.tick(SNAKE_SPEED)
    
    pygame.quit()
    quit()

# Start Game
gameLoop()
