import pygame
from dataclasses import dataclass, field


@dataclass
class Player:
    color: str
    height: float
    init_position: pygame.Vector2
    init_velocity: pygame.Vector2 = pygame.Vector2(0.0, 0.0)
    position: pygame.Vector2 = field(init=False)
    velocity: pygame.Vector2 = field(init=False)

    def __post_init__(self):
        self.position = self.init_position.copy()
        self.velocity = self.init_velocity.copy()

    def show(self, screen: pygame.Surface):
        return pygame.draw.circle(screen, self.color, self.position, self.height / 2)

    def update_position(self, screen: pygame.Surface):
        self._update_x()
        self._update_y(screen)

    def set_position(self, x: float | None = None, y: float | None = None):
        if x is not None:
            self.position.x = x
        if y is not None:
            self.position.y = y

    def set_velocity(self, x: float | None = None, y: float | None = None):
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
    G_ACC = 30.0
    JUMP_V = 15.0
    WALK_V = 5.0

    # initialize
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    display = pygame.display
    player = Player(
        color="red",
        height=80.0,
        init_position=pygame.Vector2(50.0, screen.get_height() - 80 / 2),
    )
    game_instruction = pygame.font.SysFont("Arial", 20, True)
    reset_text = game_instruction.render("Reset", True, (0, 0, 0))
    reset_button = reset_text.get_rect(topleft=(10, 10))

    # updating variables
    dt = 0
    running = True

    # functions
    def reset_game():
        player.set_position(50.0, screen.get_height() - player.height / 2)
        player.set_velocity(0, 0)

    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                    break
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and reset_button.collidepoint(event.pos):
                        reset_game()
                    break

        screen.fill("white")
        screen.blit(reset_text, reset_button)
        player.show(screen)

        keys = pygame.key.get_pressed()
        isEdgeBottom = player.position.y + player.height / 2 >= screen.get_height()
        if isEdgeBottom:
            player.set_velocity(x=0.0, y=0.0)
            if keys[pygame.K_w]:
                player.set_velocity(y=-JUMP_V)

        if keys[pygame.K_a]:
            player.set_velocity(x=-WALK_V)
        if keys[pygame.K_d]:
            player.set_velocity(x=WALK_V)

        player.update_position(screen)
        player.set_velocity(y=player.velocity.y + G_ACC * dt)

        display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
