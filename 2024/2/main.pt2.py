
def main():
    f = open("./small_input.txt", "r")

    ans = 0
    for line in f:
        l = line.split()

        violations = 0
        inc = None
        safe = False
        for i in range(len(l)):
            print(i, violations)
            l[i] = int(l[i])

            if i == 0:
                continue

            if inc is None:
                if l[i] > l[i - 1]:
                    inc = True
                elif l[i] < l[i - 1]:
                    inc = False

            if inc:
                if l[i] > l[i - 1]:
                    if l[i] - l[i - 1] < 1 or l[i] - l[i - 1] > 3:
                        violations += 1
                else:
                    violations += 1
            elif not inc:
                if l[i] < l[i - 1]:
                    if l[i - 1] - l[i] < 1 or l[i - 1] - l[i] > 3:
                        violations += 1
                else:
                    violations += 1

            if violations == 1:
                l.pop(i)
                i -= 1
                continue
            elif violations > 1:
                break

            if i == len(l) - 1:
                safe = True

        if safe:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()