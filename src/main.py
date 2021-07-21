import random
import sys

import pygame

import algorithms as a
import rendering as rd
from settings import BLOCK_SIZE, HEIGHT, WIDTH


def main():
    pygame.display.init()
    num_rectangles = ((WIDTH - BLOCK_SIZE) // BLOCK_SIZE) // 2
    max_rect_height_possible = (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE
    array = [random.randint(1, max_rect_height_possible) for _ in range(num_rectangles)]
    rd.draw_background()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        a.bubble_sort(array)


if __name__ == "__main__":
    main()
