from dataclasses import dataclass

class Point:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

numerical_keypad = {
    "7": Point(0, 0),
    "8": Point(0, 1),
    "9": Point(0, 2),
    "4": Point(1, 0),
    "5": Point(1, 1),
    "6": Point(1, 2),
    "1": Point(2, 0),
    "2": Point(2, 1),
    "3": Point(2, 2),
    "0": Point(3, 1),
    "A": Point(3, 2)
}

directional_keypad = {
    "^": Point(0, 1),
    "A": Point(0, 2),
    "<": Point(1, 0),
    "v": Point(1, 1),
    ">": Point(1, 2)
}

def get_shortest_distance(pad, symbolS, symbolD):
    if pad == "k": # Numerical Keypad
        
    elif pad == "r": # Directional Keypad

def main():
    f = open("/home/jack/projects/advent-of-code/2024/21/input.txt", "r")
    
    start, end = (-1, -1), (-1, -1)
    grid = []

    for line in f:
        grid.append(list(line.strip()))
        print(grid[-1])

        for j in range(len(grid[-1])):
            if (grid[-1][j] == 'E'):
                end = (len(grid) - 1, j)
            elif(grid[-1][j] == 'S'):
                start = (len(grid) - 1, j)

    solver = Solver(grid)
    ans = solver.solve(start[0], start[1], 'E')
    print(list(print(i) for i in solver.memo))
    
    print(list(print(i) for i in solver.cost))
    print(ans)

if __name__ == "__main__":
    main()