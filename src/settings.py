class Color:
    BACKGROUND = 0x1F363D
    RECTANGLE = 0x40798c
    HIGHLIGHTED_RECTANGLE = 0xCFE0C3


BLOCK_SIZE = 7

# Game window dimensions
WIDTH = 700
HEIGHT = 350

# To account for putting a 1 block gap around every rectangle's perimeter
WIDTH += BLOCK_SIZE
HEIGHT += BLOCK_SIZE

NUM_RECTANGLES = ((WIDTH - BLOCK_SIZE) // BLOCK_SIZE) // 2
MAX_RECT_HEIGHT_POSSIBLE = (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE

# Delay time between each frame (in milliseconds)
DELAY = 20
