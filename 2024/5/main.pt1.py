
def main():
    f = open("./input.txt", "r")

    ans = 0
    rules_input = True
    
    # The numbers that should show up after the key
    rules_after = {}

    # The numbers that should show up before the key
    rules_before = {}

    for line in f:
        l = line.split("|")
        
        if len(l) == 1:
            rules_input = False
        
        if rules_input:
            b, a = int(l[0]), int(l[1])

            if b in rules_after:
                rules_after[b].append(a)
            else:
                rules_after[b] = [a]

            if a in rules_before:
                rules_before[a].append(b)
            else:
                rules_before[a] = [b]
        else:
            l = l[0].split(",")

            for i in range(len(l)):
                l[i] = int(l[i])

            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    

if __name__ == "__main__":
    main()