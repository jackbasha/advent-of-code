import numpy as np

def main():
    f = open("/home/jbasha/projects/advent-of-code/2024/13/small_input.txt", "r")

    ans = 0
    COST_A = 3
    COST_B = 1

    coefficients = [[0 for j in range(2)] for i in range(2)]
    ordinate = [0 for i in range(2)]

    for line in f:
        line = line.split(":")
        if (len(line) < 2):
            continue
        
        xy = line[1].strip().split(",")

        if ("Button" in line[0]):
            xy[0] = int(xy[0].strip().split("X")[1])
            xy[1] = int(xy[1].strip().split("Y")[1])

            # print(line[0], xy)
            if ("Button A" in line[0]):
                coefficients[0][0] = xy[0]
                coefficients[1][0] = xy[1]
            if ("Button B" in line[0]):
                coefficients[0][1] = xy[0]
                coefficients[1][1] = xy[1]
        elif ("Prize" in line[0]):
            xy[0] = int(xy[0].strip().split("=")[1])
            xy[1] = int(xy[1].strip().split("=")[1])

            ordinate[0] = xy[0]
            ordinate[1] = xy[1]

            print(coefficients, ordinate)
            res = np.linalg.solve(coefficients, ordinate)

            print(res[1], int(res[1]))
            if (int(res[0]) == res[0] and int(res[1]) == res[1]):
                print(res)
                if (res[0] >= 0 and res[0] <= 100 and res[1] >= 0 and res[1] <= 100):
                    print(res)
                    ans += res[0] * COST_A + res[1] * COST_B

    print(ans)

if __name__ == "__main__":
    main()