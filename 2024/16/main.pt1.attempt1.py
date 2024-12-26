from enum import Enum

import numpy as np


class DIRECTIONS(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class MemoInstance:
    def __init__(self, val=None, dir=None):
        self.val = np.inf if val == None else val
        self.dir = 'Z' if dir == None else dir
    
    def __eq__(self, other):
        return self.val == other.val

    def __le__(self, other):
        return self.val <= other.val

    def __gt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return str(self.val) + ", " + self.dir

def tranlate_direction(dir):
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
        self.visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        self.memo = [[MemoInstance() for j in range(len(grid[0]))] for i in range(len(grid))]
        self.cost = [[MemoInstance() for j in range(len(grid[0]))] for i in range(len(grid))]

    def solve(self, i, j, dir, cost):
        print(i, j)

        if (self.grid[i][j] == 'E'):
            # Use for early terminating
            self.best_known_cost = min(self.best_known_cost, cost)
            self.cost[i][j] = min(self.cost[i][j], MemoInstance(cost, 'Z'))
            return MemoInstance(cost, dir)

        # if (cost >= self.best_known_cost):
        #     return np.inf

        ts = tranlate_direction(dir)
        print(ts, dir)
        
        if (self.visited[i][j]):
            ret = None

            if (dir != self.memo[i][j].dir):
                ret = MemoInstance(self.memo[i][j].val + 1000, self.memo[i][j].dir)
            else:
                ret = MemoInstance(self.memo[i][j].val, self.memo[i][j].dir)
            
            self.cost[i][j] = min(self.cost[i][j], MemoInstance(cost, dir))
            return ret
        
        self.visited[i][j] = True
        self.cost[i][j].val = cost
        self.cost[i][j].dir = dir

        if (self.grid[i][j] == '#'):
            return MemoInstance(np.inf, None)

        ts_coords = translate_direction_to_coords(dir)
        try:
            self.memo[i][j] = min(
                self.memo[i][j],
                self.solve(i + ts_coords[0], j + ts_coords[1], dir, cost + 1)
            )
        except TypeError:
            print(self.memo[i][j], self.solve(i + ts_coords[0], j + ts_coords[1], dir, cost + 1))
            exit

        for d in rotation_options(dir):
            ts = tranlate_direction(d)
            ts_coords = translate_direction_to_coords(d)

            self.memo[i][j] = min(
                self.memo[i][j],
                self.solve(i + ts_coords[0], j + ts_coords[1], d, cost + 1001)
            )

        return self.memo[i][j]

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
    ans = solver.solve(start[0], start[1], 'E', 0)
    print(list(print(i) for i in solver.memo))
    
    print(list(print(i) for i in solver.cost))
    print(ans)

if __name__ == "__main__":
    main()