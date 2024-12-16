from enum import Enum


class NumValue(Enum):
    ZERO = 0
    DOUBLE_DIGITS = 1
    OTHER = 2

class Solver:
    def __init__(self, n, blinks, arr):
        self.n = n
        self.blinks = blinks

        self.nums = {
            NumValue.ZERO: [],
            NumValue.DOUBLE_DIGITS: [],
            NumValue.OTHER: [],
        }

        for i in range(n):
            self.classify_and_append(arr[i], self.nums)

    def is_even_digits(self, i):
        return len(str(i)) % 2 == 0

    def classify_and_append(self, x, arr):
        if (x == 0):
            arr[NumValue.ZERO].append(x)
        elif (self.is_even_digits(x)):
            arr[NumValue.DOUBLE_DIGITS].append(x)
        else:
            arr[NumValue.OTHER].append(x)

    def solve(self):
        new_nums = {
            NumValue.ZERO: [],
            NumValue.DOUBLE_DIGITS: [],
            NumValue.OTHER: [],
        }

        for i in range(self.blinks):
            for v in range(len(self.nums[NumValue.ZERO])):
                new_nums[NumValue.OTHER].append(1)
            
            for v in self.nums[NumValue.DOUBLE_DIGITS]:
                l = len(str(v))
                x, y = str(v)[:l // 2], str(v)[l // 2:]
                # print(x, y)
                
                self.classify_and_append(int(x), new_nums)
                self.classify_and_append(int(y), new_nums)
            
            for v in self.nums[NumValue.OTHER]:
                self.classify_and_append(v * 2024, new_nums)

            # print(self.nums, new_nums)

            self.nums = new_nums
            new_nums = {
                NumValue.ZERO: [],
                NumValue.DOUBLE_DIGITS: [],
                NumValue.OTHER: [],
            }

            # print(self.nums, new_nums)
            # return

        return len(self.nums[NumValue.ZERO]) \
            + len(self.nums[NumValue.DOUBLE_DIGITS]) \
            + len(self.nums[NumValue.OTHER])

def main():
    f = open("./input.txt", "r")
    s = f.read().strip().split()

    l = list(map(lambda x: int(x), s))
    n = len(l)

    s = Solver(n, 25, l)
    ans = s.solve()

    print(ans)

if __name__ == "__main__":
    main()