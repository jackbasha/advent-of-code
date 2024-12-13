from enum import Enum

class NumValue(Enum):
    ZERO = 0
    DOUBLE_DIGITS = 1
    OTHER = 2

class Solver:
    def __init__(self, n, arr):
        self.n = n
        self.nums = {
            NumValue.ZERO: [],
            NumValue.DOUBLE_DIGITS: [],
            NumValue.OTHER: [],
        }

        for i in range(n):
            if (arr[i] == 0):
                self.nums[NumValue.ZERO].append(i)
            elif (self.is_even_digits(arr[i])):
                self.nums[NumValue.DOUBLE_DIGITS].append(i)
            else:
                self.nums[NumValue.OTHER].append(i)

    def is_even_digits(self, i):
        return len(str(i)) % 2 == 0

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
    s = f.read().strip().split()

    l = list(map(lambda x: int(x), s))
    n = len(l)

    s = Solver(n, l)
    ans = s.init_solve()

    print(ans)

if __name__ == "__main__":
    main()