import functools
import os
import pathlib


def part1(input_data):
    MAX_NUMBER_OF_OBJ = 3
    ans = 0
    
    input_data = input_data.splitlines()
    rows, cols = len(input_data), len(input_data[0])
    grid = [[0 for j in range(cols)] for i in range(rows)]

    ADJACENT_EIGHT = [
        (i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == j and i == 0)
    ]


    def valid_indices(x, y):
        if (x >= 0 and x < rows and y >= 0 and y < cols):
            return True
        return False

    # Build the grid
    for i in range(rows):
        for j in range(cols):
            if (input_data[i][j] == '@'):
                for x, y in ADJACENT_EIGHT:
                    new_x, new_y = x + i, y + j

                    if (valid_indices(new_x, new_y)):
                        grid[new_x][new_y] = grid[new_x][new_y] + 1

    for i in range(rows):
        for j in range(cols):
            if (input_data[i][j] == '@' and grid[i][j] <= MAX_NUMBER_OF_OBJ):
                ans += 1

    return str(ans)

def part2(input_data):
    # This solutions gets to the maximum recursion depth. Might need to make
    # another one that just keeps iterating over the grid one pass at a time
    # and only follows up with additional passes if any rolls were removed.
    # Might also be able to handle these removed indices in a queue-like
    # structure where you only push the ones that fit the criteria and handle
    # it in a BFS-like fashion
    MAX_NUMBER_OF_OBJ = 3
    ans = 0
    
    input_data = input_data.splitlines()
    rows, cols = len(input_data), len(input_data[0])
    grid = [[0 for j in range(cols)] for i in range(rows)]
    visited = [[False for j in range(cols)] for i in range(rows)]

    ADJACENT_EIGHT = [
        (i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == j and i == 0)
    ]

    def valid_indices(x, y):
        if (x >= 0 and x < rows and y >= 0 and y < cols):
            return True
        return False

    # Build the grid
    for i in range(rows):
        for j in range(cols):
            if (input_data[i][j] == '@'):
                for x, y in ADJACENT_EIGHT:
                    new_x, new_y = x + i, y + j

                    if (valid_indices(new_x, new_y)):
                        grid[new_x][new_y] = grid[new_x][new_y] + 1

    def flood_fill(x, y):
        if (visited[x][y] or grid[x][y] > 3):
            return 0

        visited[x][y] = True
        ans = 1

        for i, j in ADJACENT_EIGHT:
            new_x, new_y = x + i, y + j

            if (valid_indices(new_x, new_y)):
                grid[new_x][new_y] -= 1

                if (grid[new_x][new_y] <= 3):
                    ans += flood_fill(new_x, new_y)

        return ans

    for i in range(rows):
        for j in range(cols):
            ans += flood_fill(i, j)

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

            # if p2 != ans_b:
            #     print("Output of part 2,", p2, ", doesn't match the answer: ", ans_b)
            #     raise Exception("Output is incorrect for part 2")

def main():
    verify_against_sample_input()

    curr_dir = pathlib.Path(__file__).parent.resolve()
    input_data = get_data_from_file_path(curr_dir / "input.txt")

    p1 = part1(input_data)
    print("Answer for part 1", p1)

    p2 = part2(input_data)
    print("Answer for part 2", p2)

if __name__ == "__main__":
    main()