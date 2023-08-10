import pygame

from entities.entity import Entity


class Environment:
    def __init__(
        self,
        screen: pygame.Surface,
        clock: pygame.time.Clock,
        acceleration: float = 9.8,
        initial_velocity: float = 0,
    ):
        # default values
        self.dt: float = 1.0
        self.screen = screen
        self.clock = clock
        self._acceleration = acceleration
        self._initial_velocity = initial_velocity
        self._entities: list[Entity] = []

        # Flags
        self.running = False

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("white")
            self.apply_environment_to_entities()
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()

    def apply_environment_to_entities(self):
        for entity in self._entities:
            entity.show(self.screen)
            self._apply_gravity(entity)

    def insert_entity(self, entity: Entity):
        entity.velocity = self._initial_velocity
        self._entities.append(entity)
        return self

    def _apply_gravity(self, entity: Entity):
        entity.position.y = min(
            entity.position.y + entity.velocity,
            self.screen.get_height() - entity.size / 2,
        )
        entity.velocity = entity.velocity + self._acceleration * self.dt

    def _apply_bottom_as_ground(self, entity: Entity):
        bottom_edge = entity.position.y + entity.size
        if bottom_edge >= self.screen.get_height():
            entity.velocity = 0
