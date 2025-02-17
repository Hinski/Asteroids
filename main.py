import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidsfield import AsteroidField
from shots import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawables)
    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")
#        player.draw(screen)
#        player.update(dt)

        updatable.update(dt)
        player.timer -= dt

        for asteroid in asteroids:
            if asteroid.distance(player) <= (asteroid.radius + player.radius):
                sys.exit("Game over!")
            for shot in shots:
                if shot.distance(asteroid) <= (shot.radius + asteroid.radius):
                    shot.kill()
                    asteroid.kill()



        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60)/1000
    

if __name__ == "__main__":
    main()


