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
                    print("Upadting " + str(new_pos[0]) + "," + str(new_pos[1]) + " " + str(curr[0] + 1))
                    self.puzzle[new_pos[0]][new_pos[1]] = curr[0] + 1
                    surroundings.append((curr[0] + 1, new_pos))

        return surroundings

    def solve(self, s):
        curr = s
        q = queue.Queue()

        while (curr[1] != (70, 70)):
            print("Checking", curr)
            surr = self.visit_surrounding(curr)
            for s in surr:
                q.put(s)
            
            curr = q.get()
        
        return curr[0]

# Thoughts are simulate the first 1024 since we know that there exists a path
# up to that point, and then:
# 1. Add a good number of points (maybe around 500 or so) and see if there is a
#    path to the exit. If yes, then add 500 more, etc. Once you find that there
#    is no exit, then do a binary search-esque search for the solution between
#    the last 500 points
#   => Possible challenges: Would require saving the board state for these 500
#   points or resimulate the corrupted spots appearing
# 
# 2. Run along the path and keep a record of the currently present values in
#    each block. If a path exists, then it must be incrementing and connects to
#    a cell with the next value. Then, if a certain cell got corrupted, then
#    check its value. Use a look-up dictionary to look up other cells that have
#    the same value, and if that cell is the only one with that value, then a
#    path definitely doesn't exist. Otherwise, need to know if the other cells
#    with the same value can be used to connect a path
#   
#   e.g.,
#   100, 101, 102, 103   
#   101, 102, -1 , 104
#   102, -1 , -1 , 105 
#   103, -1 , -1 , 106
#   -1 , -1 , -1 , 107
#
#   In the above example, even though there are numerous blocks that have the
#   value 102, only one of them actually participates in a valid path. There
#   could also be multiple valid paths. Need to trace through the solution and
#   identify these cells that, even though they have a value, they are useless
#   because they cannot be used in the construction of a path.
#
#   => Possible challenges: Need to know how many paths exist and which nodes
#   participate in which paths. It could be that one node participates in
#   multiple paths

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
    print(puz.puzzle[puz.dim][puz.dim])

if __name__ == "__main__":
    main()