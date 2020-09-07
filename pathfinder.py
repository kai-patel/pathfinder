import numpy as np

class Node():

    position = None
    neighbours = None
    parent = None

    f = None
    g = None
    h = None

    visitable = None

    def __init__(self, i, j):
        self.position = (i, j)
        self.neighbours = []
        self.visitable = True

    def __repr__(self):
        return "({}, {})".format(self.position[0], self.position[1])

MAP_HEIGHT = 10
MAP_WIDTH = 10

grid = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

def printGrid(grid):
    for row in grid:
        print(row)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = Node(i, j)

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
            
            neighbour_q_distance = 1
            neighbour.g = q.g + neighbour_q_distance
            neighbour.h = h(neighbour, end)
            neighbour.f = neighbour.g + neighbour.h

            if len(list(filter(lambda x: x.position == neighbour.position and x.f < neighbour.f, open_list))) > 0:
                continue

            if len(list(filter(lambda x: x.f < neighbour.f and x.position == neighbour.position, closed_list))) > 0:
                continue

            neighbour.parent = q

            open_list.append(neighbour)

        closed_list.append(q)

    return (False, open_list, closed_list)


def h(n1, n2):
    return abs(n1.position[0] - n2.position[0]) + abs(n1.position[1] - n2.position[1])

def pathfind(firstNode, lastNode):

    found, open_list, closed_list = astarsearch(firstNode, lastNode)
    if found:
        print("Path found!")
    else:
        print("No path found")
        return []

    path = []

    while lastNode.position not in path:
        print(lastNode.parent.position)
        path.append(lastNode.position)
        lastNode = lastNode.parent
        print(path)
    
    path.append(firstNode.position)

    return reversed(list(map(str, path)))

def main():
    start = grid[0][0]
    end = grid[4][4]

    print(", ".join(pathfind(start, end)))

if __name__ == "__main__":
    main()
