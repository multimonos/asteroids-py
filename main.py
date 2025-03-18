import pygame
import sys

from shot import Shot
from asteroid import Asteroid
from asteroid_field import AsteroidField
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize
    dt = 0.0
    bgcolor = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add classes to groups
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    # instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    # asteroid = Asteroid(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 3)

    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update
        screen.fill(bgcolor)

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        # exit cond
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()

            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit(0)

        # refresh
        pygame.display.flip()
        dt = clock.tick(59) / 1000


if __name__ == "__main__":
    main()
