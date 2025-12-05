
def main():
    f = open("/home/jbasha/projects/advent-of-code/2025/1/input.txt", "r")

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
    
    print(ans)

if __name__ == "__main__":
    main()