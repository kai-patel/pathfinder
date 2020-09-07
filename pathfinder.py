import numpy as np
import pygame
import sys

class Node():

    position = None
    neighbours = None
    parent = None

    f = None
    g = None
    h = None

    visitable = None

    def __init__(self, i, j, visitable = True):
        self.position = (i, j)
        self.neighbours = []
        self.visitable = visitable

    def __repr__(self):
        return "({}, {})".format(self.position[0], self.position[1]) if self.visitable else "######"

MAP_HEIGHT = 8
MAP_WIDTH = 8

grid = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

"""
for i in range(2, len(grid)-2):
    for j in range(2, len(grid[i])-2):
        grid[i][j] = 1
"""

def printGrid(grid):
    for row in grid:
        print(row)


def genVisitableNeighbours(node):
    node_i, node_j = node.position
    neighbours = []
    #print(f"Getting neighbours for node: {node.position}")

    for i in range(node_i - 1, node_i + 2):
        for j in range(node_j - 1, node_j + 2):
            if 0 <= i < MAP_HEIGHT and 0 <= j < MAP_WIDTH:
                if not (i == node_i and j == node_j):
                    neighbour = grid[i][j]
                    if neighbour.visitable:
                        #print(f"Neighbour found! {neighbour}")
                        neighbours.append(neighbour)
    return neighbours

printGrid(grid)

def astarsearch(start: Node, end: Node):
    open_list = [start]
    closed_list = []

    while open_list:
        f_list = [i.f for i in open_list]
        q_index = np.argmin(f_list)
        q = open_list.pop(q_index)

        q.g = 0

        neighbours = genVisitableNeighbours(q)
        
        for neighbour in neighbours:

            if neighbour.position == end.position:
                neighbour.parent = q
                return (True, open_list, closed_list)

            if neighbour not in closed_list: 
                neighbour_q_distance = 1
                neighbour.g = q.g + neighbour_q_distance
                neighbour.h = h(neighbour, end)
                neighbour.f = neighbour.g + neighbour.h
                if neighbour not in open_list:
                    open_list.append(neighbour)
                    neighbour.parent = q
                else:
                    if len(list(filter(lambda x: x.position == neighbour.position and x.f < neighbour.f, open_list))) == 0:
                         open_list.append(neighbour)

        closed_list.append(q)

    return (False, open_list, closed_list)


def h(n1, n2):
    return abs(n1.position[0] - n2.position[0]) + abs(n1.position[1] - n2.position[1])

def pathfind(firstNode, lastNode):

    found, open_list, closed_list = astarsearch(firstNode, lastNode)
    if found:
        print("Path found!")
        #print(open_list)
        #print(closed_list)
    else:
        print("No path found")
        return []

    path = []

    while lastNode and lastNode.position not in path:
        #print(lastNode.parent.position)
        path.append(lastNode.position)
        lastNode = lastNode.parent
        #print(path)
    
    return reversed(path)

def main():

    pygame.init()
    size = WINDOW_W, WINDOW_H = 512, 512
    CELL_W = WINDOW_W / MAP_WIDTH
    CELL_H = WINDOW_H / MAP_HEIGHT
    
    screen = pygame.display.set_mode(size)
    surface = pygame.display.get_surface()

    editing = True
    
    

    while editing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseW, mouseH = pygame.mouse.get_pos()
                mouseW = int(mouseW//CELL_W)
                mouseH = int(mouseH//CELL_H)
                grid[mouseW][mouseH] = 1 if grid[mouseW][mouseH] == 0 else 0
                print(mouseW, mouseH)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space pressed!")
                    editing = False

        screen.fill((0, 0, 0))
        for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                width = 1 if grid[i][j] == 0 else 0
                color = (0, 255, 0) if grid[i][j] == 0 else (255, 0, 0)
                pygame.draw.rect(surface, color, pygame.Rect(i*CELL_W, j*CELL_H, CELL_W, CELL_H), width)
        
        #pygame.draw.rect(surface, (0, 255, 255), pygame.Rect(0, 0, CELL_W, CELL_H))
        pygame.display.update()


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = Node(i, j) if grid[i][j] == 0 else Node(i, j, False)

    start = grid[0][0]
    end = grid[MAP_WIDTH - 1][MAP_WIDTH - 1]

    path = pathfind(start, end)
    for i in path:
        r, c = i
        grid[r][c] = "****"

    printGrid(grid)
    print(", ".join(map(str,path)))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        screen.fill((0, 0, 0))
        for i in range(MAP_HEIGHT):
            for j in range(MAP_WIDTH):
                width = 1
                color = (0, 255, 0)
                cell = grid[i][j]
                if not isinstance(cell, Node):
                    if cell == "****":
                        width = 0
                        color = (0, 255, 255)
                else:
                    if not cell.visitable:
                        width = 0
                        color = (255, 0, 0)
                
                pygame.draw.rect(surface, color, pygame.Rect(i*CELL_W, j*CELL_H, CELL_W, CELL_H), width)

        pygame.display.update()


if __name__ == "__main__":
    main()
