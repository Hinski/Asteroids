import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidsfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatable, drawables)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawables)

    AsteroidField.containers = updatable

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
        
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60)/1000
    

if __name__ == "__main__":
    main()


