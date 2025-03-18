from typing import override
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    @override
    def draw(self, screen: pygame.Surface):
        _ = pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    @override
    def update(self, dt: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_l]:
            self.rotate(dt)

        if keys[pygame.K_j]:
            self.rotate(dt)

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt
