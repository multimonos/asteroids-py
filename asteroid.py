from typing import override

import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    @override
    def update(self, dt: float):
        self.position: pygame.Vector2 = self.position + self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        # nv0 = self.velocity.rotate(-angle)
        # nv1 = self.velocity.rotate(angle)

        nradius = self.radius - ASTEROID_MIN_RADIUS

        a0 = Asteroid(self.position.x, self.position.y, nradius)
        a1 = Asteroid(self.position.x, self.position.y, nradius)

        a0.velocity = self.velocity.rotate(-angle) * 1.2
        a1.velocity = self.velocity.rotate(angle) * 1.2
