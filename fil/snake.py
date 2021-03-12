import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake Game by Nyumat')

# Color Constants
RED = (255,0,0)
GREEN = (0,200,0)
BLUE = (0,0,255)
SHADOW = (192,192,192)
PURPLE = (102,0,102)
WHITE = (255,255,255)
BLACK = (0,0,0)
CENTER_COORDS = [200,150,10,10]

gameOver = False

x1 = 300
y1 = 300
x1_move = 0
y1_move = 0

timer = pygame.time.Clock()

while not gameOver:
      for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                  gameOver = True
            if ev.type == pygame.KEYDOWN:
                  if ev.key == pygame.K_LEFT:
                        x1_move = -10
                        y1_move = 0
                  elif ev.key == pygame.K_RIGHT:
                        x1_move = 10
                        y1_move = 0
                  elif ev.key == pygame.K_UP:
                        y1_move = -10
                        x1_move = 0
                  elif ev.key == pygame.K_DOWN:
                        y1_move = 10
                        x1_move = 0

      x1 += x1_move
      y1 += y1_move
      screen.fill(BLACK)
      pygame.draw.rect(screen,PURPLE,[x1,y1,10,10])

      pygame.display.update()

      timer.tick(30)

pygame.quit()
quit()
