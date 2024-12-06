import re

def main():
    f = open("./input.txt", "r")

    ans = 0
    for line in f:
        x = re.findall(r"mul\(\d+,\d+\)", line)
        
        for find in x:
            y = re.search(r"(\d+),(\d+)", find)
            a, b = list(map(lambda x: int(x), y.group().split(",")))
            ans += a * b
        
    print(ans)

if __name__ == "__main__":
    main()