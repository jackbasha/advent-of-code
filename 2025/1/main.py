
def part1():
    curr_dir = pathlib.Path(__file__).parent.resolve()
    f = open(curr_dir / "input.txt", "r")

    ans = 0
    curr = 50

    for l in f:
        n = int(l.strip()[1:])

        if (l[0] == "L"):
            n = n * -1

        curr = (curr + n) % 100
        print(curr)

        if (curr == 0):
            ans += 1
    
    print("Answer for part 1", ans)

def part2():
    curr_dir = pathlib.Path(__file__).parent.resolve()
    f = open(curr_dir / "input.txt", "r")

    ans = 0
    curr = 50

    for l in f:
        n = int(l.strip()[1:])

        if (l[0] == "L"):
            n = n * -1

        ans += int((curr + n) / 99)
        curr = (curr + n) % 100
        print(curr)

        if (curr == 0):
            ans += 1
    
    print("Answer for part 2", ans)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()