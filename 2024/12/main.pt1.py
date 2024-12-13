
class Solver:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m

        self.DIR_X = [1, -1, 0, 0]
        self.DIR_Y = [0, 0, 1, -1]
        
        self.visited = [[False for j in range(m)] for i in range(n)]
        self.arr = arr

    def correct_indices(self, i, j):
        return i >= 0 and i < self.n and j >= 0 and j < self.m

    def solve(self, i, j, area, perimeter, curr_letter):
        if (self.visited[i][j] == True):
            return area, perimeter
        
        self.visited[i][j] = True
        area += 1

        for d in range(4):
            new_i = i + self.DIR_X[d]
            new_j = j + self.DIR_Y[d]

            if (not self.correct_indices(new_i, new_j)):
                perimeter += 1

            if (self.correct_indices(new_i, new_j)):
                if (self.arr[new_i][new_j] == curr_letter):
                    area, perimeter = self.solve(new_i, new_j, area, perimeter, curr_letter)
                elif (self.arr[new_i][new_j] != curr_letter):
                    perimeter += 1

        return area, perimeter
    
    def init_solve(self):
        ans = 0

        for i in range(self.n):
            for j in range(self.m):
                if (self.visited[i][j] == False):
                    a, p = self.solve(i, j, 0, 0, self.arr[i][j])
                    ans += a * p

        return ans

def main():
    
    f = open("./input.txt", "r")

    ans = 0

    garden = []
    n = None
    m = None

    for line in f:
        l = list(map(lambda x: x, line.strip()))
        garden.append(l)

        if m == None:
            m = len(l)

    if n == None:
        n = len(garden)

    print(n, m)
    s = Solver(n, m, garden)
    ans = s.init_solve()

    print(ans)

if __name__ == "__main__":
    main()