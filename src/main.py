import sys

import pygame

from generate import generate_random_array
from menu import get_selection


def main():
    array = generate_random_array()
    done = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not done:
            selected_algorithm_function = get_selection()
            selected_algorithm_function(array)
        done = True


if __name__ == "__main__":
    main()
