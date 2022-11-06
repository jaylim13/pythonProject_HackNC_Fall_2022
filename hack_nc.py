import pygame
from sys import exit

# global variables
level: int = 1
score: int = 0
masks_collected = 0
OBSTACLE_START = 833
new_level = False

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
virus_surface = pygame.image.load('graphics/virus.png')
virus_rect = virus_surface.get_rect(midbottom = (15, 200))
virus_x_pos = 833
virus2_surface = pygame.image.load('graphics/virus2.png')
virus2_rect = virus2_surface.get_rect(midbottom = (15, 200))
virus2_x_pos = 833
virus3_surface = pygame.image.load('graphics/virus3.png')
virus3_rect = virus3_surface.get_rect(midbottom = (15, 200))
virus3_x_pos = 833

# Initializes the variable for the avatar, Marco
marco_surface = pygame.image.load('graphics/marco.png')
marco_rect = marco_surface.get_rect(midbottom = (15, 200))
marco_gravity = 0


# Def level function
def update_level(lvl: int) -> int:
    global new_level
    if marco_rect.right > 800:
        marco_rect.right = 10
        i = 0
        lvl += 1
        new_level = True
    return lvl


# Def score function
def update_score(scr: int) -> int:
    global masks_collected
    scr += masks_collected
    masks_collected = 0
    return scr


# Movement function
def obstacle_movement(obstacle, x_pos: int, movement_speed) -> int:
    global new_level
    x_pos += movement_speed
    if new_level:
        x_pos = 833
    elif x_pos < 1 and not new_level:
        x_pos = -100
    return x_pos


# Def difficulty
def difficulty():
    global new_level
    global level
    global virus_rect
    global virus2_rect
    global virus3_rect
    if level > 0:
        virus_rect.x = obstacle_movement(virus_surface, virus_rect.x, -2)
        screen.blit(virus_surface, virus_rect)
    if level > 1:
        virus2_rect.x = obstacle_movement(virus2_surface, virus2_rect.x, -4)
        screen.blit(virus2_surface, virus2_rect)
    if level > 2:
        virus3_rect.x = obstacle_movement(virus3_surface, virus3_rect.x, -5)
        screen.blit(virus3_surface, virus3_rect)
    new_level = False


# Loop to run the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Keyboard Controls
        if event.type == pygame.MOUSEBUTTONDOWN:
            if marco_rect.collidepoint(event.pos):
                marco_gravity = -14
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                marco_gravity = -14

        if event.type == pygame.KEYUP:
            print('key up')

    # Initializes the variable for the level label
    level_label = test_font.render(f"Level: {level}", False, 'Black')
    # Initializes the variable for the score label
    score_label = test_font.render(f"Score: {score}", False, 'Blue')
    screen.blit(landscape, (0, 0))
    screen.blit(text_surface, (293, 25))
    screen.blit(level_label, (5, 5))
    screen.blit(score_label, (670, 190))
    # Moves virus
    difficulty()
    # Moves Marco
    marco_rect.x += 2
    # Updates the level display
    level = update_level(level)
    level_label = test_font.render(f"Level: {level}", False, 'Black')
    # Updates score
    score = update_score(score)
    score_label = test_font.render(f"Score: {score}", False, 'Blue')
    if virus_rect.right <= 10: virus_rect.left = 833
    if virus2_rect.right <= 10: virus2_rect.left = 833
    if virus3_rect.right <= 10: virus3_rect.left = 833
    if marco_rect.left >= 833: marco_rect.right = 10

    marco_gravity += 1
    marco_rect.y += marco_gravity
    if marco_rect.bottom >= 200:
        marco_rect.bottom = 200

    screen.blit(marco_surface, marco_rect)
    screen.blit(virus_surface, virus_rect)

    if marco_rect.colliderect(virus_rect) or marco_rect.colliderect(virus2_rect) or marco_rect.colliderect(virus3_rect):
        print('Marco -1')
    else:
        print('Safe')

    mouse_pos = pygame.mouse.get_pos()
    if virus_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
