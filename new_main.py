import pygame
from dataclasses import dataclass, field


@dataclass
class Player:
    color: str
    height: float
    position: pygame.Vector2
    init_velocity: pygame.Vector2 = pygame.Vector2(0.0, 0.0)
    velocity: pygame.Vector2 = field(init=False)

    def __post_init__(self):
        self.velocity = self.init_velocity.copy()

    def show(self, screen: pygame.Surface):
        return pygame.draw.circle(screen, self.color, self.position, self.height / 2)

    def update_position(self, screen: pygame.Surface):
        self._update_x()
        self._update_y(screen)

    def update_velocity(self, x: float | None = None, y: float | None = None):
        if x is not None:
            self.velocity.x = x
        if y is not None:
            self.velocity.y = y

    def _update_x(self):
        self.position.x = self.position.x + self.velocity.x

    def _update_y(self, screen: pygame.Surface):
        self.position.y = min(
            self.position.y + self.velocity.y, screen.get_height() - self.height / 2
        )


def main():
    # constants
    G_ACC = 9.81

    # initialize
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    display = pygame.display
    player = Player(
        color="red",
        height=80.0,
        position=pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2),
    )

    # updating variables
    dt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        player.show(screen)

        keys = pygame.key.get_pressed()
        isEdgeBottom = player.position.y + player.height / 2 >= screen.get_height()
        if isEdgeBottom:
            player.update_velocity(x=0.0, y=0.0)
            if keys[pygame.K_w]:
                player.update_velocity(y=-10.0)

        if keys[pygame.K_a]:
            player.update_velocity(x=-5.0)
        if keys[pygame.K_d]:
            player.update_velocity(x=5.0)

        player.update_position(screen)
        player.update_velocity(y=player.velocity.y + G_ACC * dt)

        display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
