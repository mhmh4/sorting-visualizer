import pygame

from colors import CYAN, LIGHT_GRAY, DARK_GRAY, SLATE_GRAY
from screen import SCREEN
from settings import BLOCK_SIZE, DELAY_MS, HEIGHT, WIDTH


def draw_background() -> None:
    """Displays a grid background to the screen."""

    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            # outline a rectangle shape
            pygame.draw.rect(SCREEN, DARK_GRAY, rect)
            # then fill in that outline
            pygame.draw.rect(SCREEN, LIGHT_GRAY, rect, 1)


def draw_rectangles(array: list[int], highlight: int = None) -> None:
    """Displays rectangles to the screen where each rectangle's height is
    proportional to the value of the array."""

    x = BLOCK_SIZE
    for ind, val in enumerate(array):
        y = HEIGHT - (val * BLOCK_SIZE)
        rect = pygame.Rect(x, y, BLOCK_SIZE, val*BLOCK_SIZE)
        if ind == highlight:
            pygame.draw.rect(SCREEN, CYAN, rect)
        else:
            pygame.draw.rect(SCREEN, SLATE_GRAY, rect)
        # skip a block to create a gap between each rectangle
        x += BLOCK_SIZE * 2


def render(array: list[int], highlight: int = None) -> None:
    """Displays the background and the rectangles of `array`."""

    draw_background()
    pygame.display.flip()
    
    draw_rectangles(array, highlight)
    pygame.display.flip()

    pygame.time.wait(DELAY_MS) # see settings.py to modify the delay
