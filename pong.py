import pygame, sys

# General stuff
pygame.init()
clock = pygame.time.Clock()

# Window
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('SUUUUUUUUBRAU')

while True:
    # Takes input from User
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Makes sure the computer show Window (sets to 60 fps)
    pygame.display.flip()
    clock.tick(60)