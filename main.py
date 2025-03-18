import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bgcolor = (0, 0, 0)

    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update
        _ = screen.fill(bgcolor)

        # refresh
        pygame.display.flip()


if __name__ == "__main__":
    main()
