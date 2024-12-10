

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