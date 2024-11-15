import random
from turtle import width
import pygame.rect as rect
import pygame.draw as Draw


class Pipe:
    def __init__(self, bird_size, y_buffer, screen, game_speed=1):
        self.screen = screen
        self.game_speed = game_speed

        screen_width = screen.get_width()
        screen_height = screen.get_height()

        gap_top = random.randint(int(screen_height * 0.25), int(screen_height * 0.75))
        gap_bottom = gap_top + random.randint(int(bird_size * 2.5), bird_size * 5)
        self.starting_x = screen_width * 1.25

        self.gap = {
            "top": gap_top,
            "bottom": gap_bottom,
        }
        self.width = int(bird_size * 1.25)

        self.top_rect = rect.Rect(
            (self.starting_x, -y_buffer),
            (self.width, self.gap["top"] + y_buffer),
        )
        self.bottom_rect = rect.Rect(
            (self.starting_x, self.gap["bottom"]),
            (self.width, screen_height + y_buffer),
        )

        self.hit = False
        self.color = "green"

    def draw(self):
        Draw.rect(self.screen, self.color, self.top_rect)
        Draw.rect(self.screen, self.color, self.bottom_rect)

    def move(self, amount=None):
        amount = -self.game_speed if amount is None else amount

        self.top_rect.move_ip(amount, 0)
        self.bottom_rect.move_ip(amount, 0)

        if self.top_rect.x + self.top_rect.width < 0:
            self.top_rect.x = self.starting_x
            self.bottom_rect.x = self.starting_x
