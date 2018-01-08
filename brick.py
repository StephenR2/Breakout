import pygame
class Brick(pygame.sprite.Sprite):

    def __init__(self, width, color):
        super().__init__()


        self.BRICK_HEIGHT = 8
        self.BRICK_WIDTH = width
        self.BRICK_COLOR = color
        self.image = pygame.Surface((width, self.BRICK_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()


