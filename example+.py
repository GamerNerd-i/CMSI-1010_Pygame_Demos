# Example file showing a circle moving on screen
# Modified from https://www.pygame.org/docs/
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0.0

"""
For more modularity, we separate the size of our player (circle radius)
and how much we move the player each frame into their own variables.

With this change, you could also change the size or step amount during runtime,
like we do with position.
"""
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40
movement_step = 300


# This function replaces our logic from before, and adds some extra functionality
## to stop us from moving beyond the screen. Read the given documentation to learn more.
# If you make helper functions, remember to document them well so that you
## (and your groupmates) know what you've written!
def move_player(keystrokes):
    """Reads the current keystrokes and moves the player by the amount
    of pixels specified by the movement_step attribute.

    Also checks the boundaries of the screen to make sure that the player never moves
    outside them.

    Args:
        keystrokes: The sequence of key states from pygame.key.get_pressed()
    """
    if keystrokes[pygame.K_w] and (player_pos.y - player_radius) > 0:
        player_pos.y -= movement_step * dt
    if keystrokes[pygame.K_s] and (player_pos.y + player_radius) < screen.get_height():
        player_pos.y += movement_step * dt
    if keystrokes[pygame.K_a] and (player_pos.x - player_radius) > 0:
        player_pos.x -= movement_step * dt
    if keystrokes[pygame.K_d] and (player_pos.x + player_radius) < screen.get_width():
        player_pos.x += movement_step * dt


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    pygame.draw.circle(screen, "yellow", player_pos, player_radius)

    # Remember, we moved all the functionality from the loop to a function to make it
    ## more readable!
    move_player(pygame.key.get_pressed())

    pygame.display.flip()

    """
    "dt" is short for delta time: the number of seconds elapsed since
    the previous frame.
    
    In game development, it's used to make physics that don't depend on
    the game's framerate.
    
    You can see how it's used in move_player().
    """
    dt = clock.tick(60) / 1000

pygame.quit()
