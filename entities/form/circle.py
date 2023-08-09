import pygame
from entities.form import EntityParams


class CircleEntityForm:
    def show(self, screen: pygame.Surface, entity_params: EntityParams):
        pygame.draw.circle(
            screen, entity_params.color, entity_params.position, entity_params.size / 2
        )
