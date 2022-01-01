BLOCK_SIZE = 10

# Game window dimensions
WIDTH = 1000
HEIGHT = 500

# To account for putting a 1 block gap around every rectangle's perimeter
WIDTH += BLOCK_SIZE
HEIGHT += BLOCK_SIZE

NUM_RECTANGLES = ((WIDTH - BLOCK_SIZE) // BLOCK_SIZE) // 2
MAX_RECT_HEIGHT_POSSIBLE = (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE

DELAY = 20
