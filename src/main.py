import pygame

pygame.init()
clock = pygame.time.Clock()

(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()