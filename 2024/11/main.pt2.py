from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Solver:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m

        self.DIR_X = [1, -1, 0, 0]
        self.DIR_Y = [0, 0, 1, -1]
        
        self.memoization = [[None for j in range(m)] for i in range(n)]
        self.arr = [[None for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                self.arr[i][j] = arr[i][j]

    def correct_indices(self, i, j):
        return i >= 0 and i < self.n and j >= 0 and j < self.m

    def solve(self, i, j, curr):
        if self.arr[i][j] != curr:
            return 0

        if curr == 9:
            return 1

        if self.memoization[i][j] != None:
            return self.memoization[i][j]

        ans = 0
        for d in range(4):
            new_i = i + self.DIR_X[d]
            new_j = j + self.DIR_Y[d]

            if self.correct_indices(new_i, new_j):
                ans += self.solve(new_i, new_j, curr + 1)

        self.memoization[i][j] = ans

        return ans

    def init_solve(self):
        ans = 0

        for i in range(self.n):
            for j in range(self.m):
                if self.arr[i][j] == 0:
                    s = self.solve(i, j, 0)
                    print(i, j, s)
                    ans += s

        return ans

def main():
    f = open("./input.txt", "r")

    ans = 0

    topo_map = []
    n = None
    m = None

    for line in f:
        l = list(map(lambda x: int(x), line.strip()))
        topo_map.append(l)

        if m == None:
            m = len(l)

    if n == None:
        n = len(topo_map)

    print(n, m)
    s = Solver(n, m, topo_map)
    ans = s.init_solve()

    print(ans)

if __name__ == "__main__":
    main()