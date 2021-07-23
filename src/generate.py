import random

from settings import MAX_RECT_HEIGHT_POSSIBLE, NUM_RECTANGLES


def generate_random_array() -> list[int]:
    return [random.randint(1, MAX_RECT_HEIGHT_POSSIBLE)
            for _ in range(NUM_RECTANGLES)]
