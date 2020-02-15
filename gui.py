import pygame
from random import randint

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("sanke")

x, y = 10, 10  # initial positions
box = {
    'height': 50,
    'width': 50
}
speed = 5
delay = 100

# 20 X 20
length = 1
_width, _height = length, length
step = 1

matrix = []

margin_top = step
for i in range(400):
    _top = i*length + i * step
    row = []
    for j in range(400):
        _left = j*length + j * step
        rect = pygame.Rect(_left, _top, length, length)
        pygame.draw.rect(screen, (22, 111, 77), rect)
        row.append(rect)
    matrix.append(row)

pygame.display.update()

run = True
while run:
    pygame.time.delay(10)

    for ev in pygame.event.get():
        if ev.type is pygame.QUIT:
            run = False
            break
        print(ev)

    print(matrix[0][1])

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     x -= speed
    #     speed += 1
    # if keys[pygame.K_RIGHT]:
    #     x += speed
    #     speed += 1
    # if keys[pygame.K_UP]:
    #     y -= speed
    #     speed += 1
    # if keys[pygame.K_DOWN]:
    #     y += speed
    #     speed += 1
    #
    # print(x, y)
    #
    # color = (randint(0, 255), randint(0, 255), randint(0, 255))
    # screen.fill((0, 0, 0))
    # pygame.draw.rect(screen, color, (x, y, box['width'], box['height']))
    # pygame.display.update()

pygame.quit()

