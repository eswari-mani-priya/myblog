# __author__ == "Priya"

import pygame
from pygame.locals import *
import numpy as np
import time
from random import randrange


class SnakeGame:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.WIN_COLOR = (153, 204, 255)
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.width, self.height),0, 32)
        self.score = 0
        self.snake_head = [250, 250]
        self.snake_position = [[250,250],[240,250],[230,250]]
        self.apple = pygame.image.load('images/apple.jpg')
        self.apple_position = [randrange(1,50)*10, randrange(1,50)*10]

    def display_apple(self, display, apple_position, apple):
        display.blit(apple, (apple_position[0], apple_position[1]))

    def display_snake(self, snake_position):
        for position in snake_position:
            pygame.draw.rect(self.display, self.RED, pygame.Rect(position[0], position[1], 10, 10))

    def collision_with_apple(self, apple_position, score):
        apple_position = [randrange(1,50)*10, randrange(1,50)*10]
        score += 1
        return apple_position, score

    def create_snake(self, snake_head, snake_position, apple_position, button_dir, score):
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

        if snake_head == apple_position:
            apple_position, score = self.collision_with_apple(apple_position, score)
            snake_position.insert(0, list(snake_head))
        else:
            snake_position.insert(0,list(snake_head))
            snake_position.pop()
        return snake_position, apple_position, score

    def collision_with_boundaries(self, snake_head):
        if snake_head[0] >= 500 or snake_head[0] < 0 or snake_head[1] >= 500 or snake_head[1] < 0:
            return 1
        else:
            return 0

    def collision_with_self(self, snake_position):
        snake_head = snake_position[0]
        if snake_head in snake_position[1:]:
            return 1
        else:
            return 0

    def is_blocked_dir(self, snake_position, current_dir_vector):
        next_step = snake_position[0] + current_dir_vector
        snake_head = snake_position[0]
        if self.collision_with_boundaries(snake_head) == 1 or self.collision_with_self(snake_position) == 1:
            return 1
        else:
            return 0

    def play_game(self, snake_head, snake_position, apple_position, apple, button_dir, score):
        prev_button_dir = 1
        button_dir = 1
        current_dir_vector = np.array(snake_position[0]) - np.array(snake_position[1])
        collide = False

        while collide is not True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    collide = True
                if event.type == pygame.KEYDOWN:
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
            self.display.fill(self.WIN_COLOR)
            self.display_apple(self.display, apple_position, apple)
            self.display_snake(snake_position)
            snake_position, apple_position, score = self.create_snake(snake_head, snake_position, apple_position,
                                                                      button_dir, score)
            pygame.display.set_caption("Snake Game Score:"+str(score))
            pygame.display.update()
            prev_button_dir = button_dir
            if self.is_blocked_dir(snake_position, current_dir_vector) == 1:
                collide = True
            self.clock.tick(3)
        return score

    def display_score(self, display_text):
        text_font = pygame.font.Font('freesansbold.ttf', 35)
        text_surf = text_font.render(display_text, True, self.BLACK)
        text_rect = text_surf.get_rect()
        text_rect.center = ((self.width/2), (self.height/2))
        self.display.blit(text_surf, text_rect)
        pygame.display.update()
        time.sleep(2)


    def run(self):
        pygame.init()
        self.display.fill(self.WIN_COLOR)
        pygame.display.update()
        final_score = self.play_game(self.snake_head, self.snake_position, self.apple_position, self.apple, 1,
                                     self.score)
        display = pygame.display.set_mode((self.width, self.height))
        display.fill(self.WIN_COLOR)
        pygame.display.update()

        display_text = "Your Score is: "+str(final_score)
        self.display_score(display_text)

        pygame.quit()


if __name__ == "__main__":
    app = SnakeGame()
    app.run()
