class Color:
    BACKGROUND = (35, 35, 35)
    GRID = (40, 40, 40)
    RECTANGLE = (100, 119, 135)
    HIGHLIGHTED_RECTANGLE = (182, 220, 254)


BLOCK_SIZE = 10

# Game window dimensions
WIDTH = 1000
HEIGHT = 500

# To account for putting a 1 block gap around every rectangle's perimeter
WIDTH += BLOCK_SIZE
HEIGHT += BLOCK_SIZE

NUM_RECTANGLES = ((WIDTH - BLOCK_SIZE) // BLOCK_SIZE) // 2
MAX_RECT_HEIGHT_POSSIBLE = (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE

# Delay time between each frame (in milliseconds)
DELAY = 20
