import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, 
            color="pink", 
            center=self.position, 
            radius=self.radius,
            width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)           
            pos_velocity = self.velocity.rotate(rand_angle)
            neg_velocity = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = pos_velocity * 1.8
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = neg_velocity * 1.8
