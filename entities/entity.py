import pygame
from entities.form import EntityForm, EntityParams
from entities.form.circle import CircleEntityForm


class Entity:
    def __init__(
        self, entity_form: EntityForm, entity_params: EntityParams, velocity: float
    ) -> None:
        self.entity_params = entity_params
        self.size = entity_params.size
        self.position = entity_params.position

        self.velocity = velocity

        self.entity_form = entity_form

    def show(self, screen: pygame.Surface):
        self.entity_form.show(screen, self.entity_params)

    @classmethod
    def default(cls, screen: pygame.Surface):
        middle = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        default_entity_params = EntityParams(80.0, middle, "red")
        return cls(CircleEntityForm(), default_entity_params, 5.0)
