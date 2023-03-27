import pygame
from sys import exit
o = 'i'
x = pygame.init()
clock = pygame.time.Clock()

surf = pygame.display.set_mode((600,400))
pygame.display.set_caption ('UwU')

exit_game = False
game_over = False

while not exit_game:
  for event in pygame.event.get():

      if event.type == pygame.QUIT:
          exit_game = True

      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print(o)

pygame.quit()
exit()
