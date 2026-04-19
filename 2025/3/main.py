import math
import os
import pathlib
from bisect import bisect


def part1(input_data):
    ans = 0
    input_data = input_data.splitlines()
    for line in input_data:
        tens_digit = None
        ones_digit = None

        for digit_idx in range(len(line)):
            if (tens_digit is None):
                tens_digit = line[digit_idx]
            else:
                # Don't update the tens digit when considering the last digit
                # because any two digits will have a bigger number than just
                # one digit
                if (digit_idx != len(line) - 1 and line[digit_idx] > tens_digit):
                    tens_digit = line[digit_idx]
                    ones_digit = None
                elif (ones_digit is None or line[digit_idx] > ones_digit):
                    ones_digit = line[digit_idx]

        # If the biggest digit is the second to last one, take the last one as
        # the maximum to the right        
        if (ones_digit is None):
            ones_digit = line[len(line) - 1]

        ans += int(tens_digit + ones_digit)
    return str(ans)


# Unfortunately it's taking too long. Try for a more greedy solution
def part2_backtracking(input_data):
    class MemoObj:
        memoization_dict: dict[str, int]
        ongoing_max: int

        def __init__(self):
            self.memoization_dict = {}
            self.ongoing_max = -1

        def add_new_memo_if_applicable(self, curr: str):
            if (curr in self.memoization_dict):
                self.memoization_dict[curr] = max(
                    int(curr),
                    self.memoization_dict[curr]
                )
            else:
                self.memoization_dict[curr] = int(curr)

        # Return True if the current value has the potential to get bigger than the
        # current max by comparing the first `len(curr)` digits of the ongoing max
        # with the ongoing max
        # 
        # @param curr: the current string to be compared
        def can_get_bigger_than_max(self, curr: str):
            if (self.ongoing_max == -1):
                return False

            max_str = str(self.ongoing_max)

            return int(max_str[:len(curr)]) <= int(curr)

        def update_ongoing_max(self, curr: str):
            self.ongoing_max = max(
                self.ongoing_max,
                self.memoization_dict[curr]
            )

    # Need to write a recursive that tried to use the current digit or skips
    # it. The magic number of digits to be used it 12, so can set up some early
    # stops
    MAX_NUM_OF_DIGITS = 12
    ans = 0
    memo_obj = MemoObj()

    def find_best_starting_point(line: str):
        best_point = (-1, -1)

        for i in range(len(line) - MAX_NUM_OF_DIGITS):
            if (int(line[i]) > best_point[0]):
                best_point = (int(line[i]), i)
        
        return best_point[1]

    def backtracking(input, index, curr):
        # print(curr)

        # Exit early if there isn't enough digits left. `+ 1` is because the
        # element at the current index shouldn't be a part of the calculation
        if (len(curr) + len(input) - index < MAX_NUM_OF_DIGITS):
            return -1
            
        # Base condition
        if (len(curr) == MAX_NUM_OF_DIGITS):
            memo_obj.add_new_memo_if_applicable(curr)
            return memo_obj.memoization_dict[curr]

        # Return memoized result if it exists
        if (curr in memo_obj.memoization_dict):
            return memo_obj.memoization_dict[curr]

        # Yet more early prunning
        # print(memo_obj.ongoing_max)

        # Perform the calculation
        memo_obj.memoization_dict[curr] = max(
            backtracking(input, index + 1, curr + input[index]),
            backtracking(input, index + 1, curr)
        )

        memo_obj.update_ongoing_max(curr)

        return memo_obj.memoization_dict[curr]
    
    input_data = input_data.splitlines()
    for line in input_data:
        print(line)
        memo_obj = MemoObj()
        res = backtracking(line, find_best_starting_point(line), "")
        print(res)
        ans += res

    return str(ans)

def part2(input_data):
    MAX_NUM_OF_DIGITS = 12
    ans = 0

    def create_digits_dict(line: str):
        digits_dict = {}

        for i in range(len(line)):
            num = int(line[i])
            if (num not in digits_dict):
                digits_dict[num] = [i]
            else:
                digits_dict[num].append(i)

        return digits_dict
    
    def find_best_next_digit(
        digits_dict: dict[int, [int]],
        max_idx: int,
        curr_len: int,
        max_len: int
    ):
        def can_take_idx(idx: int):
            # print("Checking if can", idx, "for slot", curr_len + 1, "with", (max_len - (idx + 1)), "remaining digits")
            return (curr_len + 1 + (max_len - (idx + 1))) >= MAX_NUM_OF_DIGITS

        curr = 9
        while(curr >= 0):
            if (curr in digits_dict):
                idx = -1

                if(max_idx == -1):
                    idx = digits_dict[curr][0]
                else:
                    bisect_idx = bisect(digits_dict[curr], max_idx)
                    
                    # If found index is equal to the length of the array, then
                    # it means the best found index is longer than the array
                    if (bisect_idx == len(digits_dict[curr])):
                        curr = curr - 1
                        continue

                    idx = digits_dict[curr][bisect_idx]
                    # print(idx)

                if (can_take_idx(idx)):
                    # print("Taking", curr, "at idx", idx, "for slot", curr_len)
                    return curr, idx

            curr = curr - 1


    def build_max(digits_dict: dict[int, [int]], max_len: int):
        num = ""
        max_idx = -1

        for i in range(MAX_NUM_OF_DIGITS):
            next_digit, max_idx = find_best_next_digit(
                digits_dict,
                max_idx,
                len(num),
                max_len
            )
            num = num + str(next_digit)

        return int(num)


    input_data = input_data.splitlines()
    for line in input_data:
        # print(line)
        # print(create_digits_dict(line))
        res = build_max(create_digits_dict(line), len(line))
        # print("Result", res)
        ans += res

    return str(ans)


def get_data_from_file_path(file_path):
    f = open(file_path, "r")
    data = ""
    for line in f:
        data += line

    return data

def verify_against_sample_input():
    curr_dir = pathlib.Path(__file__).parent.resolve()
    for i in range(len(os.listdir(curr_dir)) // 2):
        example_file_name = curr_dir / "example_input_{}.txt".format(str(i))
        answer_a_file_name = curr_dir / "answer_a_{}.txt".format(str(i))
        answer_b_file_name = curr_dir / "answer_b_{}.txt".format(str(i))
        if example_file_name.is_file():
            example_data = get_data_from_file_path(example_file_name)
            ans_a = get_data_from_file_path(answer_a_file_name)
            ans_b = get_data_from_file_path(answer_b_file_name)
 
            p1 = part1(example_data)
            p2 = part2(example_data)

            if p1 != ans_a:
                print("Output of part 1,", p1, ", doesn't match the answer: ", ans_a)
                raise Exception("Output is incorrect for part 1")

            if p2 != ans_b:
                print("Output of part 2,", p2, ", doesn't match the answer: ", ans_b)
                raise Exception("Output is incorrect for part 2")

def main():
    verify_against_sample_input()

    curr_dir = pathlib.Path(__file__).parent.resolve()
    input_data = get_data_from_file_path(curr_dir / "input.txt")

    # p1 = part1(input_data)
    # print("Answer for part 1", p1)

    p2 = part2(input_data)
    print("Answer for part 2", p2)

if __name__ == "__main__":
    main()