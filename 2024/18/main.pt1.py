import numpy as np

def main():
    f = open("/home/jbasha/projects/advent-of-code/2024/18/input.txt", "r")

    dim = 70

    # Init puzzle bounds
    puzzle = [['.' for i in range(dim)] for j in range(dim)]

    lines_read = 0

    for line in f:
        
        x, y = line.split(",")

        lines_read += 1
        if(lines_read == 1024):
            break


if __name__ == "__main__":
    main()