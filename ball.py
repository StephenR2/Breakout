import pygame
import random
import time

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight):
        super().__init__()
        self.RADIUS = 10
        self.WINDOW_WIDTH = windowWidth
        self.WINDOW_HEIGHT = windowHeight
        self.color = color
        self.image = pygame.Surface((self.RADIUS, self.RADIUS))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.vx = 1
        self.vy = 1
        pygame.mixer.music.load("Blop.mp3")


#if random.random() > 0.5:  # random.random() gives a decimal between 1 and 2.
 #           vx = -vx

    def move(self):
        self.rect.top = self.rect.top + self.vy
        self.rect.right = self.rect.right + self.vx
        if self.rect.top < 0:
            self.vy = -self.vy
        if self.rect.right > self.WINDOW_WIDTH:
            self.vx = -self.vx
        if self.rect.left < 0:
            self.vx = -self.vx

    def collide_brick(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.vy = -self.vy
            pygame.mixer.music.play()

    def collide_paddle(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.vy = -self.vy
            pygame.mixer.music.play()




