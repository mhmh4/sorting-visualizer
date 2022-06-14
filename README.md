# Sorting Simulator

<div align="center">
  <img width="70%" src="assets/screenshot.png">
  <p>A single frame of merge sort being rendered by the simulator</p>
</div>

## Introduction

This is a simulator that renders sorting algorithms being performed on randomly generated arrays in real-time. The numbers that are placed within these arrays vary between the GUI's dimensions which can be customized within `settings.py`.

The delay between each frame being rendered can also be modified to your satisfaction. If you customized the GUI to be large, then consider decreasing the delay, otherwise increase the delay if you customized the GUI to be small. This will make the simulation be rendered at a good speed that can help show you the sorting algorithm works.

#### The following sorting algorithms are implemented within the application:
  - Bubble sort
  - Counting sort
  - Heapsort
  - Insertion sort
  - Merge sort
  - Quicksort
  - Selection sort

## Requirements
- Python 3.9

## Dependencies
- Pygame 2.0

## Getting Started

### You can download Pygame using `pip`, but other methods of downloading the library are available on [Pygame's website](https://pygame.org).
```
pip install pygame
```

### Run `main.py` that is within the `src` directory
```
py .\src\main.py
```
### A small GUI window should appear with a list of the sorting algorithms that you get to choose to simulate. Click on one of those options, then click the Ok button for the simulator to start rendering the algorithm.
<div align=center>
  <img width="50%" src="assets/options.png">
</div>
