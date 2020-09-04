import numpy as np

MAP_SIZE = 10
all_nodes = []

for i in range(MAP_SIZE):
    for j in range(MAP_SIZE):
        all_nodes.append((i, j))

def getNeighbours(node):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbours = []
    for d in directions:
        neighbour = tuple(sum(i) for i in zip(node, d))
        #print(neighbour)
        if neighbour in all_nodes:
            neighbours.append(neighbour)
    return neighbours

def getByCoords(i, j):
    return all_nodes[i*MAP_SIZE + j]

for i in all_nodes:
    print(getNeighbours(i))

