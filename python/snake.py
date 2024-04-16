# Simple python script to expand my python knowledge and usage of pygame

import random
import pygame
pygame.init()

# Define dimensions
d_width = 800
d_height = 600

# Create display
dis = pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption("Carson's Snake Game")

# Define color values
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Define block ize
snake_block = 10

# Create a clock and define the movement speed
clock = pygame.time.Clock()
snake_speed = 15

# Define font sizes
font_style = pygame.font.SysFont(None,50)
score_font = pygame.font.SysFont(None,35)

# Function to print current score
def your_score(score):
        value = score_font.render("Your Score:" + str(score), True, blue)
        dis.blit(value, [0, 0])

# Function that draws the snake
def our_snake(snake_block, snake_list):
        for x in snake_list:
                pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

# Function to print messages to the display
def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [d_width/4, d_height/2])
        
# Function which handles gameplay
def gameLoop():
        # Booleans used to keep game running
        gameOver = False
        gameClose = False
        
        # Starting position
        x1 = d_width/2
        y1 = d_height/2
        
        x1_change = 0
        y1_change = 0
        
        snake_List = []
        Length_of_snake = 1
        
        # Random food position
        foodx = round(random.randrange(0, d_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, d_height - snake_block) / 10.0) * 10.0
        
        # While game is still going
        while gameOver == False:
                
                # When the user loses inform user and ask to play again
                while gameClose == True:
                        dis.fill(gray)
                        message("You Lost, Q-Quit P-Play Again", blue)
                        pygame.display.update()
                        
                        # Either close the game or restart based on input
                        for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                                gameOver = True
                                                gameClose = False
                                        if event.key == pygame.K_p:
                                                gameLoop()
                # Move snake according to keyboard input
                # End game if quit is detected
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameOver = True
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        x1_change = -snake_block
                                        y1_change = 0
                                elif event.key == pygame.K_RIGHT:
                                        x1_change = snake_block
                                        y1_change = 0
                                elif event.key == pygame.K_UP:
                                        x1_change = 0
                                        y1_change = -snake_block
                                elif event.key == pygame.K_DOWN:
                                        x1_change = 0
                                        y1_change = snake_block
                # Close the game if position is outside bounds
                if x1 >= d_width or x1 < 0 or y1 >= d_height or y1 < 0:
                        gameClose = True
                        
                # Apply movement change
                x1 += x1_change
                y1 += y1_change
                
                # Paint dsiplay gray
                dis.fill(gray)  
                 
                # Create snake
                pygame.draw.rect(dis,red,[foodx,foody,snake_block,snake_block])            
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                
                # correct snake_list when length does not match
                if len(snake_List) > Length_of_snake:
                        del snake_List[0]
                        
                for x in snake_List[:-1]:
                        if x == snake_Head:     
                                gameClose = True
                
                our_snake(snake_block, snake_List)
                your_score(Length_of_snake - 1)
                
                # Draw the snake
                pygame.draw.rect(dis,black,[x1,y1,snake_block,snake_block])
                
                # Update the display
                pygame.display.update()
                
                # Find new food when snake is on food spot and increase snake and score
                if x1 == foodx and y1 == foody:
                        foodx = round(random.randrange(0, d_width - snake_block) / 10.0) * 10.0
                        foody = round(random.randrange(0, d_height - snake_block) / 10.0) * 10.0
                        Length_of_snake += 1
                        
                # Set speed
                clock.tick(snake_speed)

        # Quit game when outside the game loop
        pygame.quit()
        quit()
        
gameLoop()