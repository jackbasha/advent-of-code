from enum import Enum

import numpy as np


class DIRECTIONS(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

def translate_direction(dir):
    if (dir == 'S'):
        return DIRECTIONS.SOUTH.value
    elif (dir == 'N'):
        return DIRECTIONS.NORTH.value
    elif (dir == 'E'):
        return DIRECTIONS.EAST.value
    elif (dir == 'W'):
        return DIRECTIONS.WEST.value

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
        self.best_known_cost = np.inf
        self.visited = [[([False] * 4) for j in range(len(grid[0]))] for i in range(len(grid))]
        self.memo = [[([np.inf] * 4) for j in range(len(grid[0]))] for i in range(len(grid))]

    # Our state is i, j, and dir
    def solve(self, i, j, dir):
        # Stop condition
        if (self.grid[i][j] == 'E'):
            # Use for early terminating
            # self.best_known_cost = min(self.best_known_cost, cost)
            return 0

        # if (cost >= self.best_known_cost):
        #     return np.inf

        ts = translate_direction(dir)
        # print(ts, dir)
        
        if (self.visited[i][j][ts]):
            return self.memo[i][j][ts]
        
        self.visited[i][j][ts] = True

        if (self.grid[i][j] == '#'):
            return np.inf

        ts_coords = translate_direction_to_coords(dir)
        try:
            self.memo[i][j][ts] = min(
                self.memo[i][j][ts],
                self.solve(i + ts_coords[0], j + ts_coords[1], dir) + 1
            )
        except TypeError:
            print(self.memo[i][j], self.solve(i + ts_coords[0], j + ts_coords[1], dir, cost + 1))
            exit

        for d in rotation_options(dir):
            ts = translate_direction(d)
            ts_coords = translate_direction_to_coords(d)

            self.memo[i][j][ts] = min(
                self.memo[i][j][ts],
                self.solve(i + ts_coords[0], j + ts_coords[1], d) + 1001
            )

        return self.memo[i][j][ts]

def main():
    f = open("/home/jack/projects/advent-of-code/2024/16/small_input2.txt", "r")
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
    ans = solver.solve(start[0], start[1], 'E')
    print(list(print(i) for i in solver.memo))
    
    print(list(print(i) for i in solver.cost))
    print(ans)

if __name__ == "__main__":
    main()