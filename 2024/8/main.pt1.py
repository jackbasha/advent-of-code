

def main():
    f = open("./small_input.txt", "r")

    ans = 0

    symbol_locations = {}
    n = None
    m = None

    i = 0
    j = 0

    for line in f:
        j = 0
        for c in line:
            if c != '.' and c != '\n':
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

    print(antinodes, len(antinodes), len(antinodes[0]))

    print(ans)

if __name__ == "__main__":
    main()