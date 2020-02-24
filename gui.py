import pygame
from random import randint

pygame.init()

# square sizes = 10 x 10
length = 20
no_squares = {
    'height': 30,
    'width': 50
}
square_width, square_height = length, length
margin = 1

# window set up
width = (no_squares['width'] * length) + (margin * no_squares['width'])
height = (no_squares['height'] * length) + (margin * no_squares['height'])
size = width, height
screen = pygame.display.set_mode(size)
pygame.display.set_caption('snake')

# clock
DELAY = 100

# colors
GREEN = (22, 111, 77)
BROWN = (100, 77, 11)
RED = (153, 51, 0)

# matrix in which we store each Rect object
matrix = []

for i in range(no_squares['height']):
    _top = i * length + i * margin
    row = []
    for j in range(no_squares['width']):
        _left = j * length + j * margin
        rect = pygame.Rect(_left, _top, length, length)
        pygame.draw.rect(screen, GREEN, rect)
        row.append(rect)
    matrix.append(row)

direction = {
    'x': 1,
    'y': 0
}

# random point
random_x, random_y = randint(0, no_squares['height'] - 1), randint(0, no_squares['width'] - 1)
pygame.draw.rect(screen, RED, matrix[random_x][random_y])
pygame.display.update()

x, y = no_squares['height'] // 2, no_squares['width'] // 2
# a list of tuples (x, y)
tail = [[x, y], [x + 1, y], [x + 2, y]]
for i in tail:
    pygame.draw.rect(screen, BROWN, matrix[i[0]][i[1]])
pygame.display.update()

print(tail)

run = True
while run:
    pygame.time.delay(DELAY)
    for ev in pygame.event.get():
        if ev.type is pygame.QUIT:
            run = False
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction['x'] = 0
        direction['y'] = -1
    if keys[pygame.K_RIGHT]:
        direction['x'] = 0
        direction['y'] = 1
    if keys[pygame.K_UP]:
        direction['x'] = -1
        direction['y'] = 0
    if keys[pygame.K_DOWN]:
        direction['x'] = 1
        direction['y'] = 0

    # last element of the tail
    last_x = tail[len(tail) - 1][0]
    last_y = tail[len(tail) - 1][1]

    if len(tail) > 1:
        for i in range(len(tail) - 1, 0, -1):
            # print(tail[i], '=', tail[i-1])
            tail[i][0] = tail[i - 1][0]
            tail[i][1] = tail[i - 1][1]

    tail[0][0] = tail[0][0] + direction['x']
    tail[0][1] = tail[0][1] + direction['y']

    if tail[0][0] == no_squares['height']:
        tail[0][0] = 0
    if tail[0][1] == no_squares['width']:
        tail[0][1] = 0
    if tail[0][0] == -1:
        tail[0][0] = no_squares['height'] - 1
    if tail[0][1] == -1:
        tail[0][1] = no_squares['width'] - 1

    if (tail[0][0], tail[0][1]) == (random_x, random_y):
        tail.append([last_x, last_y])
        random_x, random_y = randint(0, no_squares['height'] - 1), randint(0, no_squares['width'] - 1)
        while [random_x, random_y] in tail:
            # random point
            random_x, random_y = randint(0, no_squares['height'] - 1), randint(0, no_squares['width'] - 1)
        pygame.draw.rect(screen, RED, matrix[random_x][random_y])
    else:
        pygame.draw.rect(screen, GREEN, matrix[last_x][last_y])
    pygame.draw.rect(screen, BROWN, matrix[tail[0][0]][tail[0][1]])

    pygame.display.update()

pygame.quit()

