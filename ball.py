import pygame
import time

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight):
        """
        Sets the constants of the ball
        :param color: Gets color
        :param windowWidth: Gets width of game window
        :param windowHeight: Gets height of game window.
        """
        super().__init__()
        self.RADIUS = 10
        self.WINDOW_WIDTH = windowWidth
        self.WINDOW_HEIGHT = windowHeight
        self.color = color
        self.image = pygame.Surface((self.RADIUS, self.RADIUS))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.vx = 5
        self.vy = 3
        pygame.mixer.music.load("Blop.mp3")



    def move(self):
        """
        Moving the ball, making sure if it hits the wall to reverse the direction of the ball to make
        sure the ball doesn't move off of the screen.

        """
        self.rect.top = self.rect.top + self.vy
        self.rect.right = self.rect.right + self.vx
        if self.rect.top < 0:
            self.vy = -self.vy
        if self.rect.right > self.WINDOW_WIDTH:
            self.vx = -self.vx
        if self.rect.left < 0:
            self.vx = -self.vx

    def collide_brick(self, spriteGroup):
        """
        If ball collides with the brickgroup reverse the y direction and the x direction
        play sound
        :param spriteGroup: Get the group it is interacting with.
        :return: Returns new vy and vx upon collision
        """
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.vy = -self.vy
            self.vx = -self.vx
            pygame.mixer.music.play()

    def collide_paddle(self, spriteGroup, paddlerect):
        """
        If ball collide with paddle on the left change the y and x direction
        If ball collide with paddle on the right change the y and x direction
        If ball collide with paddle on the center slow the x
        :param spriteGroup: Gets the spritegroup that its interacting with.
        Plays music each time collide happens.
        :param paddlerect: Gets paddle dimensions
        :return: Returns new vx and vy values
        """
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.vy = -self.vy
            if self.rect.left < paddlerect.left + 20:
                self.vx = 6
            elif self.rect.left < paddlerect.left + 40:
                self.vx = 2
            elif self.rect.left < paddlerect.left + 60:
                self.vx = -9
            pygame.mixer.music.play()
