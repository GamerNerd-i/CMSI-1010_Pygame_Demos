import pygame
import pygame.rect as rect
import pygame.display as Display
import pygame.draw as Draw
import pygame.font as font
import random

GRAVITY = 0.2
GAME_SPEED = 2

MAX_PIPES = 4
PIPE_Y_BUFFER = 10

pygame.init()
screen = Display.set_mode((720 // 2, 1280 // 2))
clock = pygame.time.Clock()

HEIGHT = screen.get_height()
WIDTH = screen.get_width()

BIRD_SIZE = WIDTH // 10


class Pipe:
    def __init__(self):
        gap_top = random.randint(int(HEIGHT * 0.25), int(HEIGHT * 0.75))
        gap_bottom = gap_top + random.randint(int(BIRD_SIZE * 2.5), BIRD_SIZE * 5)
        self.starting_x = WIDTH * 1.25

        self.gap = {
            "top": gap_top,
            "bottom": gap_bottom,
        }
        self.width = int(BIRD_SIZE * 1.25)

        self.top_rect = rect.Rect(
            (self.starting_x, -PIPE_Y_BUFFER),
            (self.width, self.gap["top"] + PIPE_Y_BUFFER),
        )
        self.bottom_rect = rect.Rect(
            (self.starting_x, self.gap["bottom"]),
            (self.width, HEIGHT + PIPE_Y_BUFFER),
        )

        self.hit = False
        self.color = "green"

    def draw(self):
        Draw.rect(screen, self.color, self.top_rect)
        Draw.rect(screen, self.color, self.bottom_rect)

    def move(self, amount=-GAME_SPEED):
        self.top_rect.move_ip(amount, 0)
        self.bottom_rect.move_ip(amount, 0)

        if self.top_rect.x + self.top_rect.width < 0:
            self.top_rect.x = self.starting_x
            self.bottom_rect.x = self.starting_x


class Bird:
    def __init__(self):
        self.radius = BIRD_SIZE // 2
        self.flap_size = 5
        self.speed = 0
        self.x, self.y = WIDTH // 3, HEIGHT // 2
        self.alive = True
        self.hitbox = rect.Rect(
            (self.x - (self.radius * 0.8), self.y - (self.radius * 0.78)),
            (BIRD_SIZE * 0.8, BIRD_SIZE * 0.8),
        )

    def draw(self):
        # Draw.rect(screen, "black", self.hitbox)
        Draw.circle(screen, "blue", (self.x, self.y), self.radius)

    def move(self):
        self.y += self.speed
        self.hitbox.y += self.speed
        self.speed += GRAVITY

        self.out_of_bounds()

    def flap(self):
        self.speed = -self.flap_size

    def check_hit_pipe(self, pipe):
        if self.hitbox.collidelist([pipe.top_rect, pipe.bottom_rect]) >= 0:
            self.alive = False

    def out_of_bounds(self):
        if self.y - self.radius > HEIGHT:
            self.alive = False


bird_y = screen.get_height() / 2
bird_x = screen.get_width() / 3

player = Bird()
pipes = []
pipe_gap = 2.5


for pipe_num in range(MAX_PIPES):
    new_pipe = Pipe()
    new_pipe.move(new_pipe.width * pipe_gap * pipe_num)
    pipes.append(new_pipe)

score = 0

text_size = 100
text = font.Font(None, text_size)
game_over_text = [
    (text.render("Game", True, "red"), (WIDTH // 3, HEIGHT // 2 - text_size // 2)),
    (text.render("Over!", True, "red"), (WIDTH // 3, HEIGHT // 2 + text_size // 2)),
]
score_text = text.render("Score: " + str(score), True, "black")


def move_all():
    player.move()
    for pipe in pipes:
        pipe.move()
        player.check_hit_pipe(pipe)


def draw_all():
    player.draw()
    for pipe in pipes:
        pipe.draw()


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

    Display.flip()
    clock.tick(60)


pygame.quit()
