import pathlib
import os


def part1(input_data):
    ans = 0
    curr = 50

    input_data = input_data.split("\n")
    # print(input_data)

    for l in input_data:
        n = int(l.strip()[1:])

        if (l[0] == "L"):
            n = n * -1

        curr = (curr + n) % 100
        # print(curr)

        if (curr == 0):
            ans += 1
    
    return str(ans)

def part2(input_data):
    ans = 0
    curr = 50

    input_data = input_data.split("\n")
    # print(input_data)

    for l in input_data:
        n = int(l.strip()[1:])

        if (l[0] == "L"):
            n = n * -1

        # if ((curr + n) % 100 != 0):

        # If it's a one pass through 0, add one to the answer
        print("Before adding", curr, curr + n)

        # if (curr < 0 and (curr + n) > 0):
        #     print("Cond 1 true")

        # if (curr > 0 and (curr + n) < 0):
        #     print("Cond 2 true")

        if ((curr < 0 and (curr + n) > 0) or (curr > 0 and (curr + n) < 0)):
            # print("One of the conds is true")
            ans += 1

        # Count the extra spins
        print("Extra spins for", abs(curr + n), "are", (abs(curr + n) // 100))

        # If we land on 0, we're counting one extra
        if ((curr + n) % 100 == 0):
            ans -= 1

        ans += (abs(curr + n) // 100)

        curr = (curr + n) % 100
        # print(curr)

        if (curr == 0):
            ans += 1

        print("After adding", curr, ans)
    
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
                print("Output of part 1 `" + p1 + "` doesn't match the answer:", ans_a)

            if p2 != ans_b:
                print("Output of part 2 `" + p2 + "` doesn't match the answer:", ans_b)

def main():
    verify_against_sample_input()

    curr_dir = pathlib.Path(__file__).parent.resolve()
    input_data = get_data_from_file_path(curr_dir / "input.txt")

    # p1 = part1(input_data)
    # p2 = part2(input_data)

    # print("Answer for part 1", p1)
    # print("Answer for part 2", p2)

if __name__ == "__main__":
    main()