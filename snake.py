import pygame, random, time
from pygame.locals import *


def random_grid_number():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def snake_collision(c1, tail):
    for c2 in tail:
        if (c1[0] == c2[0]) and (c1[1] == c2[1]):
            return True

def border_colision(snake):
    return (snake[0] > 590 or snake[0] < 0 or
            snake[1] > 590 or snake[1] < 0)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200), (190,200), (180,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = random_grid_number()

my_direction = RIGHT

clock = pygame.time.Clock()

while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if my_direction == DOWN:
                    pass
                else:
                    my_direction = UP
            if event.key == K_DOWN:
                if my_direction == UP:
                    pass
                else:
                    my_direction = DOWN
            if event.key == K_LEFT:
                if my_direction == RIGHT:
                    pass
                else:
                    my_direction = LEFT
            if event.key == K_RIGHT:
                if my_direction == LEFT:
                    pass
                else:
                    my_direction = RIGHT

    # Changing directions with key arrows
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # Changing the head position
    if collision(snake[0], apple_pos):
        apple_pos = random_grid_number()
        snake.append((0,0))

    # Checking if the snake hits itself
    if snake_collision(snake[0], snake[1:]):
        time.sleep(3)
        pygame.quit()
    
    # Checking to see if the snake goes out of the border   
    if border_colision(snake[0]):
        time.sleep(3)
        pygame.quit()

    # Changing the position of the tail
    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # Creating first apple
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()