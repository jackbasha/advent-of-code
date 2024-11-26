
def main():
    f = open("./input.txt", "r")
    ans = 0
    DEBUG_OUTPUT = False
    skip_game = False
    for line in f:
        game_number, pulls = line.split(":")
        game_number = int(game_number.split(" ")[1])

        if(game_number == 72):
            DEBUG_OUTPUT = True

        pulls_array = pulls.split(";")

        for pull in pulls_array:
            pairs = pull.strip().split(",")
            if(DEBUG_OUTPUT):
                print(pairs)

            for pair in pairs:
                amount, color = pair.strip().split(" ")
                amount = int(amount)
                
                if(DEBUG_OUTPUT):
                    print(amount, color)

                if(
                    (color == "red" and amount > 12)
                 or (color == "green" and amount > 13)
                 or (color == "blue" and amount > 14)
                ):
                    if(DEBUG_OUTPUT):
                        print("CAUGHT")
                    skip_game = True
        
        if(DEBUG_OUTPUT):
            print(pulls_array)

        if(not skip_game):
            ans += game_number
        
        DEBUG_OUTPUT = False
        skip_game = False
    
    print(ans)


if __name__ == "__main__":
    main()