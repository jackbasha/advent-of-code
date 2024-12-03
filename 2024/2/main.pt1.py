
def main():
    f = open("./input.txt", "r")

    ans = 0
    for line in f:
        l = line.split()

        inc = None
        safe = False
        for i in range(len(l)):
            l[i] = int(l[i])

            if i == 0:
                continue

            if inc is None:
                if l[i] > l[i - 1]:
                    inc = True
                elif l[i] < l[i - 1]:
                    inc = False
                else:
                    break

            if inc:
                if l[i] > l[i - 1]:
                    if l[i] - l[i - 1] < 1 or l[i] - l[i - 1] > 3:
                        break
                else:
                    break
            elif not inc:
                if l[i] < l[i - 1]:
                    if l[i - 1] - l[i] < 1 or l[i - 1] - l[i] > 3:
                        break
                else:
                    break

            if i == len(l) - 1:
                safe = True

        if safe:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()