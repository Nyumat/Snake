import pygame
import time
import random as rand 

pygame.init()

# Screen/Font Configuration
SCREEN_WIDE = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDE,SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game by Nyumat')
FONT = pygame.font.SysFont("bahnschrift",30, bold=True,italic=True)
SCORE_FONT = pygame.font.SysFont("comicsans",35)

# Color Constants
RED = (255,0,0)
GREEN = (0,200,0)
BLUE = (0,0,255)
SHADOW = (192,192,192)
PURPLE = (102,0,102)
WHITE = (255,255,255)
BLACK = (0,0,0)
CENTER_COORDS = [200,150,10,10]


timer = pygame.time.Clock()

# Snake Constants
SNAKE_BLOCK = 10
SPEED = 15

def initSnake(SNAKE_BLOCK,SNAKE_BODY):
      for i in SNAKE_BODY:
            pygame.draw.rect(screen,RED, [i[0], i[1], SNAKE_BLOCK, SNAKE_BLOCK])

def displayMessage(message,colour):
      text = FONT.render(message,True,colour)
      screen.blit(text,[SCREEN_WIDE/6, SCREEN_HEIGHT/3])

def displayScore(score):
      total_score = SCORE_FONT.render("Score: " + str(score), True, GREEN)
      screen.blit(total_score, [0,0])

def start():

      snake = []
      snake_len = 1

      gameOver = False
      closed = False

      x1 = SCREEN_WIDE / 2
      y1 = SCREEN_HEIGHT / 2

      x1_move = 0
      y1_move = 0

      foo = round(rand.randrange(0 , SCREEN_WIDE - SNAKE_BLOCK) / 10.0) * 10.0
      bar = round(rand.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

      while not gameOver:

            while closed == True:
                  screen.fill(BLACK)
                  displayMessage("Loss. Q to quit or P to play again." , RED)
                  displayScore(snake_len - 1)
                  pygame.display.update()

                  for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                              if event.key == pygame.K_q:
                                    gameOver = True
                                    closed = False
                              if event.key == pygame.K_p:
                                    start()

            for move in pygame.event.get():
                  if move.type == pygame.QUIT:
                              gameOver = True
                  if move.type == pygame.KEYDOWN:
                        if move.key == pygame.K_LEFT:
                              x1_move = -SNAKE_BLOCK
                              y1_move = 0
                        elif move.key == pygame.K_RIGHT:
                              x1_move = SNAKE_BLOCK
                              y1_move = 0
                        elif move.key == pygame.K_UP:
                              y1_move = -SNAKE_BLOCK
                              x1_move = 0
                        elif move.key == pygame.K_DOWN:
                              y1_move = SNAKE_BLOCK
                              x1_move = 0

            # If the user exit's the screen (edges)
            if x1 >= SCREEN_WIDE or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
                  closed = True
      
            x1 += x1_move
            y1 += y1_move

            screen.fill(BLACK)
            pygame.draw.rect(screen, BLUE, [foo, bar, SNAKE_BLOCK, SNAKE_BLOCK])

            f_snake = []
            f_snake.append(x1)
            f_snake.append(y1)
            snake.append(f_snake)

            if len(snake) > snake_len:
                  del snake[0]

            for k in snake[:-1]:
                  if k == f_snake:
                        closed = True
            
            initSnake(SNAKE_BLOCK, snake)
            displayScore(snake_len  - 1)

            pygame.display.update()

            if x1 == foo and y1 == bar:
                  foo = round(rand.randrange(0, SCREEN_WIDE - SNAKE_BLOCK) / 10.0) * 10.0
                  bar = round(rand.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
                  snake_len += 1

            timer.tick(SPEED)

      pygame.quit()
      quit()

start()