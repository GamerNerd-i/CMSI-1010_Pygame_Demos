from pickle import FALSE
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))  # surface

player_x = 250
player_y = 250

amogus = pygame.image.load("Red.png")  # surface

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")

    keystrokes = pygame.key.get_pressed()
    if keystrokes[pygame.K_UP]:
        player_y -= 3
    if keystrokes[pygame.K_DOWN]:
        player_y += 3
    if keystrokes[pygame.K_LEFT]:
        pygame.transform.flip(amogus, True, False)
        player_x -= 3
    if keystrokes[pygame.K_RIGHT]:
        pygame.transform.flip(amogus, True, False)
        player_x += 3

    screen.blit(amogus, (player_x, player_y))

    pygame.display.flip()

pygame.quit()
