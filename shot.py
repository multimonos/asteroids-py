from typing import override

import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, SHOT_RADIUS
        )

    @override
    def update(self, dt: float):
        self.position: pygame.Vector2 = self.position + self.velocity * dt
