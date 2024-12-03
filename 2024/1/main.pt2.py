
def main():
    f = open("./input.txt", "r")

    l1, l2 = [], []
    for line in f:
        i1, i2 = line.split()
        l1.append(int(i1))
        l2.append(int(i2))

    dict = {}

    for i in range(len(l2)):
        if l2[i] in dict:
            dict[l2[i]] += 1
        else:
            dict[l2[i]] = 1

    ans = 0
    for i in l1:
        if i in dict:
            ans += i * dict[i]

    print(ans)

if __name__ == "__main__":
    main()