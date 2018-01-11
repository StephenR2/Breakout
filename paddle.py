import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color):
        """
        Sets constants of the paddle.
        :param color: Gets color of the paddle
        """
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10
        self.RECTCOLOR = color
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, mouseposition):
        """
        Ensures the paddle follows the mouse and the paddle is centered with the cursor.
        :param mouseposition: Gets position of the mouse.
        :return: Returns position of paddle.
        """

        if mouseposition[0] >= 0 and mouseposition[0] <= 400:
            self.rect.centerx = mouseposition[0]

