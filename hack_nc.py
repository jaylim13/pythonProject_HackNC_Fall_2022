import pygame
from sys import exit

# Creates screen for the game to be played
pygame.init()
screen = pygame.display.set_mode((833, 218))
pygame.display.set_caption("Marco vs Covid")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/small_pixel.ttf', 30)

# Initializes the variable for the background and text
landscape = pygame.image.load('graphics/landscape.jpg')
text_surface = test_font.render('Marco vs Covid', False, 'Red')

# Initializes the variable for COVID-19
virus_surface = pygame.image.load('graphics/CC_virus.png')
virus_rect = virus_surface.get_rect(midbottom = (15, 200))
virus_x_pos = 833

# Initializes the variable for the avatar, Marco
marco_surface = pygame.image.load('graphics/CC_Marco.png')
#_pos = 10
#marco_y_pos = 140

marco_surface = pygame.image.load('graphics/CC_Marco.png')
marco_rect = marco_surface.get_rect(midbottom = (15, 200))

marco_gravity = 0

# Loop to run the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if marco_rect.collidepoint(event.pos):
                marco_gravity = -14
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                marco_gravity = -14

        if event.type == pygame.KEYUP:
            print('key up')


    screen.blit(landscape, (0, 0))
    screen.blit(text_surface, (300, 25))
    # Moves virus
    screen.blit(virus_surface, virus_rect)
    # Moves Marco
    #TODO
    virus_rect.x -= 2
    marco_rect.x += 1


    if virus_rect.right <= 10: virus_rect.left = 833
    if marco_rect.left >= 833: marco_rect.right = 10


    marco_gravity += 1
    marco_rect.y += marco_gravity
    if marco_rect.bottom >= 200 : marco_rect.bottom = 200

    screen.blit(marco_surface, marco_rect)
    screen.blit(virus_surface, virus_rect)



    if marco_rect.colliderect(virus_rect):
        print('Marco -1')
    else:
        print('Safe')

    mouse_pos = pygame.mouse.get_pos()
    if virus_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60)
