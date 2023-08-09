import pygame

from entities.entity import Entity
from environment import Environment


def main():
    # pygame setup
    pygame.init()
    window_size = (1280, 720)
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    display = pygame.display

    player1 = Entity.default(screen)
    environment = Environment(screen, clock)
    environment.insert_entity(player1)
    environment.run()


if __name__ == "__main__":
    main()
