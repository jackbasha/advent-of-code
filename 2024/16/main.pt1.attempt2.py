from heapq import *

import numpy as np


def translate_direction_to_coords(dir):
    if (dir == 'S'):
        return (1, 0)
    elif (dir == 'N'):
        return (-1, 0)
    elif (dir == 'E'):
        return (0, 1)
    elif (dir == 'W'):
        return (0, -1)

def rotation_options(dir):
    if (dir == 'S' or dir == 'N'):
        return ('E', 'W')
    elif (dir == 'E' or dir == 'W'):
        return ('N', 'S')

class Solver:
    def __init__(self, grid):
        self.grid = grid
        # self.DIRECTIONS = ['S', 'N', 'E', 'W']
        self.cost = [[np.inf for j in range(len(grid[0]))] for i in range(len(grid))]

    def solve(self, i, j, dir, cost):
        # heappush(queue, (cost, (next item), direction))

        queue = []
        heappush(queue, (0, (i, j), dir))

        while (len(queue) > 0):
            cost, loc, d = heappop(queue)
            # print(loc, cost)``

            if (self.grid[loc[0]][loc[1]] == 'E'):
                return cost

            if (self.cost[loc[0]][loc[1]] != np.inf):
                continue
            
            if (self.grid[loc[0]][loc[1]] == '#'):
                continue

            ts_coords = translate_direction_to_coords(d)
            heappush(
                queue,
                (cost + 1, (loc[0] + ts_coords[0], loc[1] + ts_coords[1]), d)
            )

            for ro in rotation_options(d):
                ts_coords = translate_direction_to_coords(ro)

                heappush(
                    queue,
                    (cost + 1001, (loc[0] + ts_coords[0], loc[1] + ts_coords[1]), ro)
                )

def main():
    f = open("/home/jack/projects/advent-of-code/2024/16/input.txt", "r")
    start, end = (-1, -1), (-1, -1)
    grid = []

    for line in f:
        grid.append(list(line.strip()))
        print(grid[-1])

        for j in range(len(grid[-1])):
            if (grid[-1][j] == 'E'):
                end = (len(grid) - 1, j)
            elif(grid[-1][j] == 'S'):
                start = (len(grid) - 1, j)

    solver = Solver(grid)
    ans = solver.solve(start[0], start[1], 'E', 0)
    # print(list(print(i) for i in solver.memo))
    
    # print(list(print(i) for i in solver.cost))
    print(ans)

if __name__ == "__main__":
    main()