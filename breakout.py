import ball
import brick
import paddle
import pygame
import sys
from pygame.locals import *


def main():
    pygame.init()
    pygame.font.init()

    #  Constants that will be used in the program
    FPS = 60
    fpsClock = pygame.time.Clock()
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW - 1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    NUM_TURNS = 3
    brickGroup = pygame.sprite.Group()
    ballGroup = pygame.sprite.Group()
    paddleGroup = pygame.sprite.Group()
    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption("Breaker")
    mainSurface.fill(WHITE)
    xposition = 0
    yposition = BRICK_Y_OFFSET
    list_of_colors = [RED, ORANGE, YELLOW, GREEN, CYAN]
    drawBall = ball.Ball(RED, APPLICATION_WIDTH, APPLICATION_HEIGHT)
    drawBall.rect.x = 200
    drawBall.rect.y = 300
    ballGroup.add(drawBall)
    mainSurface.blit(drawBall.image, drawBall.rect)
    for color in list_of_colors:
        for y in range(2):
            for x in range(BRICKS_PER_ROW):
                brickOne = brick.Brick(BRICK_WIDTH, color)
                brickOne.rect.x = xposition
                brickOne.rect.y = yposition
                mainSurface.blit(brickOne.image, brickOne.rect)
                brickGroup.add(brickOne)
                xposition = xposition + (BRICK_WIDTH + BRICK_SEP)
            xposition = 0
            yposition = yposition + BRICK_HEIGHT + BRICK_SEP
    paddletest = paddle.Paddle(WHITE)
    paddletest.rect.centerx = APPLICATION_WIDTH / 2
    paddletest.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    mainSurface.blit(paddletest.image, paddletest.rect)
    paddleGroup.add(paddletest)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        mainSurface.fill(BLACK)
        paddletest.move(pygame.mouse.get_pos())
        mainSurface.blit(paddletest.image, paddletest.rect)
        mainSurface.blit(drawBall.image, drawBall.rect)
        drawBall.move()
        if drawBall.rect.bottom > APPLICATION_HEIGHT:
            drawBall.rect.x = APPLICATION_WIDTH / 2
            drawBall.rect.y = APPLICATION_HEIGHT / 2
            mainSurface.blit(drawBall.image, drawBall.rect)
            pygame.time.wait(100)
            NUM_TURNS = NUM_TURNS - 1
        if NUM_TURNS == 0:
            pygame.mixer.music.load("Heartbeat.mp3")
            pygame.mixer.music.play()
            mainSurface.fill(BLACK)
            myfont = pygame.font.SysFont('Helvetica', 30)
            textsurface = myfont.render('Game Over!', False, RED)
            XTEXT = (APPLICATION_WIDTH / 2) - 60
            YTEXT = (APPLICATION_HEIGHT / 2) - 60
            mainSurface.blit(textsurface, (XTEXT, YTEXT))
            pygame.display.update()
            pygame.time.wait(3000)
            sys.exit()
            pygame.quit()
        bricksprites = brickGroup.sprites()
        if len(bricksprites) == 0:
            pygame.mixer.music.load("Cheering.mp3")
            pygame.mixer.music.play()
            myfontwin = pygame.font.SysFont('Helvetica', 30)
            textsurfacewin = myfontwin.render('You Win!', False, GREEN)
            XTEXT = (APPLICATION_WIDTH / 2) - 60
            YTEXT = (APPLICATION_HEIGHT / 2) - 60
            mainSurface.blit(textsurfacewin, (XTEXT, YTEXT))
            pygame.display.update()
            pygame.time.wait(1500)
            sys.exit()
            pygame.quit()

        drawBall.collide_brick(brickGroup)
        drawBall.collide_paddle(paddleGroup, paddletest.rect)

        for bricks in brickGroup:
            mainSurface.blit(bricks.image, bricks.rect)
        pygame.display.update()
        fpsClock.tick(FPS)

main()
