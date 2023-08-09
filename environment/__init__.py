import pygame

from entities.entity import Entity


class Environment:
    def __init__(
        self,
        screen: pygame.Surface,
        clock: pygame.time.Clock,
        acceleration: float = 0.02,
        initial_velocity: float = 5.0,
        loop: bool = False,
    ):
        # default values
        self.dt: float = 0.0
        self.screen = screen
        self.clock = clock
        self._acceleration = acceleration
        self._initial_velocity = initial_velocity
        self._entities = []

        # Flags
        self.running = False
        self._loop = loop

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
        entity.position.y = entity.position.y + self._initial_velocity
        entity.velocity = entity.velocity + self._acceleration * self.dt

    def _apply_edge_loop(self, entity: Entity):
        bottom_edge = entity.position.y + entity.size
        if bottom_edge > self.screen.get_height():
            pass
