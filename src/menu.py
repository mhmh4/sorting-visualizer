import tkinter

class Menu:
    ...

def update_selection(new_selection):
    selection = new_selection

options = (
    "Bubble sort",
    "Counting sort",
    "Heap sort",
    "Insertion sort",
    "Merge sort",
    "Quicksort",
    "Selection sort"
)

root = tkinter.Tk()
root.geometry("200x150")

selection = tkinter.StringVar(root)
selection.set(options[0])

w = tkinter.OptionMenu(root, selection, *options, command=update_selection)
w.pack()

print(selection)
b = tkinter.Button(root, text="Go", command=None)
b.pack()

tkinter.mainloop()
