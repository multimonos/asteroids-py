import pygame
from asteroid import Asteroid
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

    # add classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)

    # instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = Asteroid(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 3)

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

        # refresh
        pygame.display.flip()
        dt = clock.tick(59) / 1000


if __name__ == "__main__":
    main()
