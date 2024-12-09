
def find_ops(res, numbers, i, acc):
    if i == len(numbers):
        return acc == res
    
    if i == 0:
        return find_ops(res, numbers, i + 1, numbers[i])
    else:
        return find_ops(res, numbers, i + 1, acc + numbers[i]) or \
                find_ops(res, numbers, i + 1, acc * numbers[i]) or \
                find_ops(res, numbers, i + 1, int(str(acc) + str(numbers[i])))

def main():
    f = open("./input.txt", "r")

    ans = 0
    for line in f:
        l = line.split(":")
        res = int(l[0])
        numbers = l[1].strip().split()
        numbers = list(map(lambda x: int(x), numbers))

        if find_ops(res, numbers, 0, 0):
            ans += res

    print(ans)

if __name__ == "__main__":
    main()