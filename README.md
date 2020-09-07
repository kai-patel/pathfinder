# pathfinder

A simple python application to demonstrate the A* search algorithm

## Introduction

Written in Python using some NumPy, as well as pygame for GUI support. The application demonstrates the A* search algorithm on a grid.The user can click to add/remove "walls" on the grid, which the algorithm will try to find a path around.

## Usage

Simply run pathfinder.py using Python 3.7+.

```bash
py -3 ./pathfinder.py
```

The default window size is 512x512, with an 8x8 grid size. These constants can be changed in the source code through MAP_HEIGHT/MAP_WIDTH and WINDOW_H/WINDOW_W. The size of each cell on the grid will adjust to fit the window.
