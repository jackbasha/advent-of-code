
def main():
    f = open("./input.txt", "r")

    l1, l2 = [], []
    for line in f:
        i1, i2 = line.split()
        l1.append(int(i1))
        l2.append(int(i2))

    l1.sort()
    l2.sort()

    for i in range(len(l1)):
        l1[i] = abs(l1[i] - l2[i])

    print(sum(l1))

if __name__ == "__main__":
    main()