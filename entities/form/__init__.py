import pygame
from dataclasses import dataclass
from typing import Protocol


@dataclass
class EntityParams:
    size: float
    position: pygame.Vector2
    color: str


class EntityForm(Protocol):
    def show(self, screen: pygame.Surface, entity_params: EntityParams):
        ...
