"""

This file uses the aocd library to fetch input and create a new day. If the
token/session expired, then get another one using the guide in
https://github.com/wimglenn/advent-of-code-wim/issues/1

"""

from aocd.models import Puzzle
import shutil
import pathlib
import sys
import itertools
import os

def main():
    y, d = map(lambda x: int(x), sys.argv[1:])
    p = Puzzle(year=y, day=d)

    curr_dir = pathlib.Path(__file__).parent.resolve()
    dir_to_make = curr_dir / "{}/{}".format(y, d)

    if dir_to_make.is_dir():
        print("Folder already exists, refetching input only...")
    else:
        os.makedirs(dir_to_make)
        shutil.copy(curr_dir / "_init_main_file.py", dir_to_make / "main.py")

    # Write input data to input.txt file
    f = open(dir_to_make / "input.txt", "w")
    f.write(p.input_data)

    for i in range(len(p.examples)):
        example_file_name = "example_input_{}.txt".format(str(i))
        example_file = open(dir_to_make / example_file_name, "w")
        example_file.write(p.examples[i].input_data)

        answer_a_file_name = "answer_a_{}.txt".format(str(i))
        answer_a_file = open(dir_to_make / answer_a_file_name, "w")
        answer_a_file.write(p.examples[i].answer_a)

        answer_b_file_name = "answer_b_{}.txt".format(str(i))
        answer_b_file = open(dir_to_make / answer_b_file_name, "w")
        answer_b_file.write(p.examples[i].answer_b)


if __name__ == "__main__":
    main()