import numpy as np
import queue

class Puzzle:
    def __init__(self):
        # Init puzzle bounds
        self.dim = 71

        self.puzzle = [[np.inf for i in range(self.dim)] for j in range(self.dim)]
        # self.visited = [[False for i in range(self.dim)] for j in range(self.dim)]
        
        self.directions = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]
    
    def within_bounds(self, pos, dir):
        if (pos[0] + dir[0] < self.dim
            and pos[1] + dir[1] < self.dim
            and pos[0] + dir[0] >= 0
            and pos[1] + dir[1] >= 0
            and self.puzzle[pos[0] + dir[0]][pos[1] + dir[1]] != -1
        ):
            return True

        return False

    def visit_surrounding(self, curr):
        pos = curr[1]
        surroundings = []

        for dir in self.directions:
            if (self.within_bounds(pos, dir)):
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if (self.puzzle[new_pos[0]][new_pos[1]] > curr[0] + 1):
                    self.puzzle[new_pos[0]][new_pos[1]] = curr[0] + 1
                    surroundings.append((curr[0] + 1, new_pos))

        return surroundings

    def solve(self, s):
        curr = s
        q = queue.Queue()

        while (curr[1] != (70, 70)):
            surr = self.visit_surrounding(curr)
            for s in surr:
                q.put(s)
            
            curr = q.get()
        
        return curr[0]

def main():
    f = open("/home/jbasha/projects/advent-of-code/2024/18/input.txt", "r")

    puz = Puzzle()
    lines_read = 0

    for line in f:
        x, y = map(lambda x: int(x), line.split(","))
        puz.puzzle[x][y] = -1

        lines_read += 1
        if(lines_read == 1024):
            break
    
    puz.solve((0, (0, 0)))
    print(puz.puzzle[puz.dim - 1][puz.dim - 1])

if __name__ == "__main__":
    main()