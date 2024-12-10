
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def mul(self, k):
        return Point(self.x * k, self.y * k)

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
                    symbol_locations[c].append(Point(i, j))
                else:
                    symbol_locations[c] = [Point(i, j)]
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

                antinodes[a.x][a.y] = True
                antinodes[b.x][b.y] = True

                d = a - b

                k = 1
                a_prime = a + d.mul(k)

                while(a_prime.x >= 0 and a_prime.x < n and a_prime.y >= 0 and a_prime.y < m):
                    antinodes[a_prime.x][a_prime.y] = True
                    k += 1
                    a_prime = a + d.mul(k)

                k = 1
                b_prime = b - d.mul(k)
                while(b_prime.x >= 0 and b_prime.x < n and b_prime.y >= 0 and b_prime.y < m):
                    antinodes[b_prime.x][b_prime.y] = True
                    k += 1
                    b_prime = b - d.mul(k)

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