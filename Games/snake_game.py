# __author__ == "Priya"

import pygame
from pygame.locals import *
import numpy as np
import random
import time
import sys


class SnakeGame:
    def show_apple(self, apple, apple_pos):
        self.DISPLAYSURF.blit(apple, tuple(apple_pos))

    def show_snake(self, snake_pos):
        for pos in snake_pos:
            pygame.draw.rect(self.DISPLAYSURF, self.RED, pygame.Rect(pos[0], pos[1], 10, 10))

    def ate_apple(self, score):
        apple_pos = [random.randrange(1,100)*10, random.randrange(1,100)*10]
        score += 1
        return apple_pos, score

    def hit_boundaries(self, snake_head):
        if snake_head[0] >= 1000 or snake_head[0]<0 or snake_head[1]>=500 or snake_head[1]<0:
            return 1
        else:
            return 0

    def  hit_with_self(self, snake_pos):
        snake_head = snake_pos[0]
        if snake_head in snake_pos[1:]:
            return 1
        else:
            return 0

    def run_snake(self, snake_head, snake_pos, apple_pos, button_dir, score):
        if button_dir == 1:
            snake_head[0] += 10
        elif button_dir == 0:
            snake_head[0] -= 10
        elif button_dir == 2:
            snake_head[1] += 10
        elif button_dir == 3:
            snake_head[1] -= 10
        else:
            pass

        if snake_head == apple_pos:
            apple_pos, score = self.ate_apple(score)
            snake_pos.insert(0,list(snake_head))
        else:
            snake_pos.insert(0,list(snake_head))
            snake_pos.pop()
        return snake_pos, apple_pos, score

    def is_dir_blocked(self, snake_pos, current_directions):
        next = snake_pos[0]+current_directions
        snake_head = snake_pos[0]
        if self.hit_boundaries(snake_head) == 1 or self.hit_with_self(snake_pos) == 1:
            return 1
        else:
            return 0

    def display_final_score(self, Score_display):
        text_font = pygame.font.Font('freesansbold.ttf', 50)
        show_text = text_font.render(Score_display, True, self.BLACK)
        text_rect = show_text.get_rect()
        text_rect.center = ((500, 500))
        self.DISPLAYSURF.blit(show_text, text_rect)
        pygame.display.update()
        time.sleep(2)

    def __init__(self):
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((1000,1000),0,32)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.WINDOW_COLOR = (200, 200, 200)
        self.DISPLAYSURF.fill(self.WINDOW_COLOR)
        apple = pygame.image.load('images/apple.jpg')
        self.clock = pygame.time.Clock()
        score = 0
        #Defining apple and snake positions
        snake_head = [500,500]
        snake_position = [[500,500], [540, 500], [530, 500]]
        apple_position = [random.randrange(1,100)*10, random.randrange(1,100)*10]
        pygame.display.set_caption('Snake Game SCORE: ' + str(score))
        collide = False
        # button directions
        prev_button_dir = 1
        button_dir = 1
        current_directions = np.array(snake_position[0]) - np.array(snake_position[1])
        while collide is not True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    collide = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and prev_button_dir != 1:
                        button_dir = 0
                    elif event.key == pygame.K_RIGHT and prev_button_dir != 0:
                        button_dir = 1
                    elif event.key == pygame.K_UP and prev_button_dir != 2:
                        button_dir = 3
                    elif event.key == pygame.K_DOWN and prev_button_dir != 3:
                        button_dir = 2
                    else:
                        button_dir = button_dir
            self.show_apple(apple, apple_position)
            self.show_snake(snake_position)
            # New Snake, apple positions and Score
            snake_pos, apple_pos, score = self.run_snake(snake_head, snake_position, apple_position, button_dir, score)
            pygame.display.set_caption('Snake Game SCORE: ' + str(score))
            pygame.display.update()
            prev_button_dir = button_dir
            if self.is_dir_blocked(snake_pos, current_directions) == 1:
                collide = True
        pygame.quit()

SnakeGame()

