import pygame
import sys

from asteroid      import Asteroid
from asteroidfield import AsteroidField
from constants     import SCREEN_HEIGHT, SCREEN_WIDTH
from logger        import log_state, log_event
from player        import Player
from shot          import Shot

def main():
    pygame.init()
    clock  = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt     = 0.0

    shots     = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()

    Player.containers        = (updatable, drawable)
    Asteroid.containers      = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers          = (updatable, drawable, shots)

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player   = Player(player_x, player_y)

    asteroidField = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
