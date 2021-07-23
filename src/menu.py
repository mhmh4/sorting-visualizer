from typing import Callable

import tkinter

from algorithms import *

OPTIONS = {
    "Bubble sort": bubble_sort,
    "Counting sort": counting_sort,
    "Heap sort": heap_sort,
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
    "Quicksort": quicksort,
    "Selection sort": selection_sort
}


def get_selection() -> Callable[[list[int]], None]:
    tkinter.mainloop()
    return OPTIONS[selection.get()]


root = tkinter.Tk()
root.eval("tk::PlaceWindow . center")

selection = tkinter.StringVar(root)
selection.set("Bubble sort")

w = tkinter.OptionMenu(root, selection, *OPTIONS)
w.pack(side=tkinter.LEFT)

b = tkinter.Button(root, text="Ok", command=lambda: root.destroy())
b.pack(side=tkinter.RIGHT)
