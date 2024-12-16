import functools

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

    def mod(self, mod_x, mod_y):
        return Point(self.x % mod_x, self.y % mod_y)

class Robot:
    def __init__(self, p, v):
        self.p = Point(p[1], p[0])
        self.v = Point(v[1], v[0])

    def calculate_position(self, seconds):
        self.p = self.p + self.v.mul(seconds)

class Solver:
    def __init__(self, n, m, seconds, robots):
        self.n = n
        self.m = m
        self.seconds = seconds
        self.robots = robots

    def calculate_quadrant(self, p):
        if (p.x == self.n // 2 or p.y == self.m // 2):
            return -1

        if (p.x < self.n // 2 and p.y < self.m // 2):
            return 0
        elif (p.x < self.n // 2 and p.y > self.m // 2):
            return 1
        elif (p.x > self.n // 2 and p.y < self.m // 2):
            return 2
        elif (p.x > self.n // 2 and p.y > self.m // 2):
            return 3
    
    def calculate_safety_factor(self):
        quadrants = [0, 0, 0, 0]
        for robot in self.robots:
            if (self.calculate_quadrant(robot.p) == -1):
                continue

            quadrants[self.calculate_quadrant(robot.p)] += 1

        return functools.reduce(lambda x, y: x * y, quadrants)

    def calculate_positions(self, seconds):
        for robot in self.robots:
            robot.calculate_position(seconds)
            robot.p = robot.p.mod(self.n, self.m)

    def print_map(self):
        grid = [[0 for j in range(self.m)] for i in range(self.n)]

        for robot in self.robots:
            grid[robot.p.x][robot.p.y] += 1

        for row in grid:
            print(row)

    def solve(self):
        self.calculate_positions(self.seconds)
        return self.calculate_safety_factor()

def main():
    f = open("/home/jbasha/projects/advent-of-code/2024/14/input.txt", "r")

    n, m = f.readline().strip().split(",")
    robots = []

    for line in f:
        p, v = line.strip().split(" ")

        p = p.split("=")[1].split(",")
        v = v.split("=")[1].split(",")

        p = list(map(lambda x: int(x), p))
        v = list(map(lambda x: int(x), v))

        robots.append(Robot(p, v))

    s = Solver(int(n), int(m), 100, robots)
    ans = s.solve()
    s.print_map()

    print(ans)

if __name__ == "__main__":
    main()