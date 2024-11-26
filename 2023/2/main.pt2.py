
def main():
    f = open("./input.txt", "r")
    ans = 0
    for line in f:
        game_number, pulls = line.split(":")
        pulls_array = pulls.split(";")

        mins = {"red": 0, "green": 0, "blue": 0}

        for pull in pulls_array:
            pairs = pull.strip().split(",")

            for pair in pairs:
                amount, color = pair.strip().split(" ")
                amount = int(amount)

                mins[color] = max(mins[color], amount)
        
        set_power = 1
        for k, v in mins.items():
            set_power = set_power * v

        ans += set_power
        
        
    print(ans)


if __name__ == "__main__":
    main()