import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color):
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10
        self.RECTCOLOR = color
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, mouseposition):


        if mouseposition[0] >= 0 and mouseposition[0] <= 400:
            self.rect.centerx = mouseposition[0]


