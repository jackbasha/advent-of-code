"""

This file uses the aocd library to fetch input and create a new day. If the
token/session expired, then get another one using the guide in
https://github.com/wimglenn/advent-of-code-wim/issues/1

"""

from aocd import get_data
import shutil
import pathlib
import sys
import itertools
import os

def main():
    y, d = map(lambda x: int(x), sys.argv[1:])
    curr_dir = pathlib.Path(__file__).parent.resolve()

    dir_to_make = curr_dir / "{}/{}".format(y, d)

    if dir_to_make.is_dir():
        print("Folder already exists")
        sys.exit(1)

    os.makedirs(dir_to_make)
    shutil.copy(curr_dir / "_temp_file.py", dir_to_make / "main.py")

    f = open(dir_to_make / "input.txt", "w")
    f.write(get_data(day=d, year=y))

if __name__ == "__main__":
    main()