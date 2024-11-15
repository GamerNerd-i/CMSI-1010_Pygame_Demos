import pygame
import pygame.display as Display
import pygame.font as font

from pipe import Pipe
from bird import Bird

GRAVITY = 0.3
GAME_SPEED = 1

MAX_PIPES = 4
PIPE_Y_BUFFER = 10

pygame.init()
screen = Display.set_mode((720 // 2, 1280 // 2))
clock = pygame.time.Clock()

HEIGHT = screen.get_height()
WIDTH = screen.get_width()

BIRD_SIZE = WIDTH // 10


def new_game(pipe_gap=2.5):
    bird_y = screen.get_height() / 2
    bird_x = screen.get_width() // 3
    player = Bird(BIRD_SIZE, GRAVITY, screen)
    pipes = []
    for pipe_num in range(MAX_PIPES):
        new_pipe = Pipe(BIRD_SIZE, PIPE_Y_BUFFER, screen)
        new_pipe.move(new_pipe.width * pipe_gap * pipe_num)
        pipes.append(new_pipe)

    return player, pipes, 0, bird_y, bird_x


player, pipes, score, bird_y, bird_x = new_game()


def move_all():
    player.move()
    for pipe in pipes:
        pipe.move()
        player.check_hit_pipe(pipe)


def draw_all():
    player.draw()
    for pipe in pipes:
        pipe.draw()


score = 0

text_size = 100
text = font.Font(None, text_size)
game_over_text = [
    (text.render("Game", True, "red"), (WIDTH // 3, HEIGHT // 2 - text_size // 2)),
    (text.render("Over!", True, "red"), (WIDTH // 3, HEIGHT // 2 + text_size // 2)),
]
score_text = text.render("Score: " + str(score), True, "black")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("skyblue")
    draw_all()

    if player.alive:
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            player.flap()
        move_all()

        for pipe in pipes:
            if pipe.top_rect.x + pipe.width == player.x - player.radius:
                score += 1

        score_text = text.render("Score: " + str(score), True, "black")
        screen.blit(score_text, (WIDTH // 20, HEIGHT // 20))
    else:
        screen.blits(game_over_text)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            player, pipes, score, bird_y, bird_x = new_game()

    Display.flip()
    clock.tick(60)


pygame.quit()
