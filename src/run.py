import contextlib
import sys

with contextlib.redirect_stdout(None):
    import pygame

import generate
import algorithms


def run():
    if len(sys.argv) < 2:
        print("Usage: sorting algorithm name")
        return
    choice = sys.argv[1].lower()
    match choice:
        case "bubble":
            selection = algorithms.bubble_sort
        case "counting":
            selection = algorithms.counting_sort
        case "heap":
            selection = algorithms.heapsort
        case "insertion":
            selection = algorithms.insertion_sort
        case "merge":
            selection = algorithms.merge_sort
        case "odd-even":
            selection = algorithms.odd_even_sort
        case "quick":
            selection = algorithms.quicksort
        case "selection":
            selection = algorithms.selection_sort
        case _:
            print(f"Invalid selection: '{choice}'")
            return
    array = generate.generate_random_array()
    done = False
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if not done:
                selection(array)
            done = True
    except KeyboardInterrupt:
        print()
        pass


if __name__ == "__main__":
    run()
