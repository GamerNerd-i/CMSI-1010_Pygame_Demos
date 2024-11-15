import pygame.rect as rect
import pygame.draw as Draw


class Bird:
    def __init__(self, bird_size, gravity, screen):
        self.screen = screen
        self.gravity = gravity

        self.radius = bird_size // 2
        self.flap_size = 4
        self.speed = 0
        self.x, self.y = self.screen.get_width() // 3, self.screen.get_height() // 2
        self.alive = True
        self.hitbox = rect.Rect(
            (self.x - (self.radius * 0.8), self.y - (self.radius * 0.8)),
            (bird_size * 0.8, bird_size * 0.8),
        )

    def draw(self):
        Draw.rect(self.screen, "black", self.hitbox)
        Draw.circle(self.screen, "blue", (self.x, self.y), self.radius)

    def move(self):
        self.y += self.speed
        self.hitbox.y = self.y - (self.radius * 0.8)
        self.speed += self.gravity

        self.out_of_bounds()

    def flap(self):
        self.speed = -self.flap_size

    def check_hit_pipe(self, pipe):
        if self.hitbox.collidelist([pipe.top_rect, pipe.bottom_rect]) >= 0:
            self.alive = False

    def out_of_bounds(self):
        if self.y - self.radius > self.screen.get_height():
            self.alive = False
