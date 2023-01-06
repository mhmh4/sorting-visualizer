import sys

import pygame

import generate
import algorithms


def main():
    if len(sys.argv) < 2:
        print("Usage: sorting algorithm name or id")
        return
    choice = sys.argv[1].lower()
    match choice:
        case "1" | "bubble":    selection = algorithms.bubble_sort
        case "2" | "counting":  selection = algorithms.counting_sort
        case "3" | "heap":      selection = algorithms.heapsort
        case "4" | "insertion": selection = algorithms.insertion_sort
        case "5" | "merge":     selection = algorithms.merge_sort
        case "6" | "odd-even":  selection = algorithms.odd_even_sort
        case "7" | "quick":     selection = algorithms.quicksort
        case "8" | "selection": selection = algorithms.selection_sort
        case _:
            print(f"Invalid selection: '{choice}'")
            return

    array = generate.generate_random_array()
    done = False
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if not done:
                selection(array)
            done = True
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
