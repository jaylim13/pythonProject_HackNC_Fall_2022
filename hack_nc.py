import pygame
from sys import exit

# Starts up a screen for the game to be played
pygame.init()
screen = pygame.display.set_mode((833, 218))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/small_pixel.ttf', 50)

# Initializes the variable for the background and text
landscape = pygame.image.load('graphics/landscape.jpg')
text_surface = test_font.render('My game', False, 'Green')

# Initializes the variable for COVID-19
virus_surface = pygame.image.load('graphics/virus.jpeg')
virus_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(landscape, (0, 0))
    screen.blit(text_surface, (300, 50))
    virus_x_pos += 1
    screen.blit(virus_surface, (virus_x_pos, 100))
    pygame.display.update()
    clock.tick(60)

    pygame.display.update()
