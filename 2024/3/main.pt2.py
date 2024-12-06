import re

def main():
    f = open("./input.txt", "r")

    do = True
    ans = 0

    for line in f:
        x = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line)

        for find in x:
            if "don't" in find:
                do = False
            elif "do" in find:
                do = True
            elif do:
                y = re.search(r"(\d+),(\d+)", find)
                a, b = list(map(lambda x: int(x), y.group().split(",")))
                ans += a * b

    print(ans)

if __name__ == "__main__":
    main()