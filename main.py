import pygame
from pygame.locals import K_SPACE, KEYDOWN

# initialize game
pygame.init()

# set up window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
window = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])

# arrow loaded from image and resized
arrow = pygame.image.load("arrow.png").convert_alpha()
arrow = pygame.transform.scale(arrow, (400, 400))

# Timer for smooth framerate
clock = pygame.time.Clock()

# Running loop
running = True
while running:

    # Background filled as white
    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 0), (SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2), SCREEN_WIDTH / 3, 10)
    window.blit(arrow, (SCREEN_HEIGHT / 3, SCREEN_WIDTH / 3))

    # User clicks window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # Rotate arrow on keypress
                arrow = pygame.transform.rotate(arrow, 1)


    # Update initial state
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
