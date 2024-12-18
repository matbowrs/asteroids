import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, drawable, updatable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    game_clock = pygame.time.Clock() 
    dt = 0
    HIGH_SCORE = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.check_collision(player_1):
                print("Game over!")
                print(f"Your score is: {HIGH_SCORE}")
                print(f"You shot down {int(HIGH_SCORE / 5)} asteroids!")
                sys.exit()
            for bullet in shots:
                # check if bullet collides with asteroid object
                if bullet.check_collision(obj):
                    HIGH_SCORE += 5
                    obj.split()

        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Divide by 1000 t convert from milliseconds to seconds
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
