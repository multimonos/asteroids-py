import pygame
from typing import Self


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.Surface):
        raise NotImplementedError("implement this in a child class")

    def update(self, dt: float):
        raise NotImplementedError("implement this in a child class")

    def collides_with(self, other: Self):
        return self.position.distance_to(other.position) <= (self.radius + other.radius)
