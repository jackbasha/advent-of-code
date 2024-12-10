
class Solver:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        
        self.arr = [[None for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                self.arr[i][j] = arr[i][j]

    # There is a huge room for memoization here if a number can reach k many
    # 9's, then that can be momized and reused in future iterations

    # Current thought is how to record the number of 9's that can be reached
    # and without passing a truth table as a parameter as that's quite
    # inefficient... Maybe define it as a class variable?

    def solve(self, i, j):
        if(self.arr[i][j] == '.'):

def main():
    f = open("./input.txt", "r")

    ans = 0

    symbol_locations = {}
    n = None
    m = None

    i = 0
    j = 0

    for line in f:
        j = 0
        for c in line:
            if i == 0:
                print(c, j)
            if c == '\n':
                continue

            if c != '.':
                if c in symbol_locations:
                    symbol_locations[c].append((i, j))
                else:
                    symbol_locations[c] = [(i, j)]
            j += 1

        if m == None:
            m = j
        i += 1

    if n == None:
        n = i

    antinodes = [[False for j in range(m)] for i in range(n)]

    for c in symbol_locations:
        for i in range(len(symbol_locations[c])):
            for j in range(i + 1, len(symbol_locations[c])):
                a = symbol_locations[c][i]
                b = symbol_locations[c][j]

                d = (a[0] - b[0], a[1] - b[1])

                anti1 = (a[0] + d[0], a[1] + d[1])
                anti2 = (b[0] - d[0], b[1] - d[1])

                if anti1[0] >= 0 and anti1[0] < n and anti1[1] >= 0 and anti1[1] < m:
                    antinodes[anti1[0]][anti1[1]] = True

                if anti2[0] >= 0 and anti2[0] < n and anti2[1] >= 0 and anti2[1] < m:
                    antinodes[anti2[0]][anti2[1]] = True

    for i in range(n):
        for j in range(m):
            if antinodes[i][j]:
                print("#", end = "")
                ans += 1
            else:
                print(".", end = "")
        print()

    print(ans)

if __name__ == "__main__":
    main()