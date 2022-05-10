import pygame, sys
import os


# General stuff
pygame.init()
clock = pygame.time.Clock()

# Window
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('SUUUUUUUUBARU')

# Sets background
background_size = width, height = (1920, 1080)
background_surface = pygame.Surface(background_size)
background = pygame.image.load('C:/Users/Sephley/Documents/GitHub/subaru-simulator/test_image.jpg')
screen.blit(background, (0, 0))
pygame.display.update()  # or pygame.display.flip()

while True:
    # Takes input from User
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Makes sure the computer shows Window (sets to 60 fps)
    pygame.display.flip()
    clock.tick(60)