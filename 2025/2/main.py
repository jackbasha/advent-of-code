import os
import pathlib


def duplicated_digits(s):
    # print(s, int(str(s) + str(s)))
    return int(str(s) + str(s))

def get_half_digits_rounded_down(n):
    # print(n)
    n = str(n)

    if (len(n) == 1):
        return int(n)

    halved_n = n[:len(n) // 2]
    # print(n, halved_n)
    return int(halved_n)


def part1(input_data):
    """
    First thoughts: Let the ranges be l, r. Take `l` and and grab half the
    digits rounded down (For 998, you would have 9. But for 1234, you would
    have 12). Call this split digits rounded down `n`.

    Then, do a loop `n, n+1, ..., n+k` where k is the first number such that
    `(n+k)(n+k)` > r: 
        For each iteration, duplicate `n` into `nn` and convert them into a
        number. If the number is in [l, r], then add it to the total.
    """
    ans = 0

    for ran in input_data:
        l, r = ran.split("-")
        s = get_half_digits_rounded_down(l)

        l, r = int(l), int(r)
        while(duplicated_digits(s) <= r):
            # print("Found", duplicated_digits(s))
            if (duplicated_digits(s) >= l):
                ans += duplicated_digits(s)
            s += 1

    print(ans, str(ans))
    return str(ans)

def part2(input_data):
    """
    Sorta similar to the first part but don't just trim half the number for
    every s, but try to try to keep duplicating while you're getting a number
    less than r.

    Start with the very first digit as s and keep duplicating until you get a
    number that's bigger than l, then keep duplicating while it's less than r
    and add those numbers to the invalid IDs. Afterwards, increase s,
    duplicate, rinse and repeat.
    """
    ans = 0
    return str(ans)


def get_data_from_file_path(file_path):
    f = open(file_path, "r")
    data = ""
    for line in f:
        data += line

    if ("input" in file_path.parts[-1]):
        ranges = data.split(",")
        for i in range(len(ranges)):
            ranges[i] = ranges[i].strip()

        return ranges
    else:
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

            if p2 != ans_b:
                print("Output of part 2,", p2, ", doesn't match the answer: ", ans_b)

def main():
    verify_against_sample_input()

    curr_dir = pathlib.Path(__file__).parent.resolve()
    input_data = get_data_from_file_path(curr_dir / "input.txt")

    p1 = part1(input_data)
    print("Answer for part 1", p1)

    # p2 = part2(input_data)
    # print("Answer for part 2", p2)

if __name__ == "__main__":
    main()