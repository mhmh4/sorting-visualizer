BLOCK_SIZE = 25

# Screen dimensions
WIDTH = 1000
HEIGHT = 300

# Every rectangle will have at least a 1 block gap around its perimeter
WIDTH += BLOCK_SIZE
HEIGHT += BLOCK_SIZE

NUM_RECTANGLES = ((WIDTH - BLOCK_SIZE) // BLOCK_SIZE) // 2
MAX_RECT_HEIGHT_POSSIBLE = (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE

# For larger screen dimensions, decrease the delay time
DELAY_MS = 50 # in milliseconds
