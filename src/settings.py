BLOCK_SIZE = 10

# Screen dimensions
WIDTH = 1000
HEIGHT = 500

# Every rectangle will have at least a 1 block gap around its perimeter
WIDTH += BLOCK_SIZE
HEIGHT += BLOCK_SIZE

NUM_RECTANGLES = ((WIDTH - BLOCK_SIZE) // BLOCK_SIZE) // 2
MAX_RECT_HEIGHT_POSSIBLE = (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE

# For larger screen dimensions, decrease the delay time
DELAY_MS = 13 # in milliseconds
