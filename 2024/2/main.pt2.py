def backtrack(l, prev_idx, curr_idx, violations, inc):
    print(prev_idx, curr_idx, violations, inc)

    if violations > 1:
        return False

    if curr_idx == len(l):
        return True

    safe = True

    if prev_idx != None:
        if inc is None:
            if l[curr_idx] > l[prev_idx]:
                inc = True
            elif l[curr_idx] < l[prev_idx]:
                inc = False

        if inc:
            if l[curr_idx] > l[prev_idx]:
                if l[curr_idx] - l[prev_idx] < 1 or l[curr_idx] - l[prev_idx] > 3:
                    safe = False
            else:
                safe = False
        elif not inc:
            if l[curr_idx] < l[prev_idx]:
                if l[prev_idx] - l[curr_idx] < 1 or l[prev_idx] - l[curr_idx] > 3:
                    safe = False
            else:
                safe = False

    if safe == False and violations > 0:
        # Save some time by returning early if we're already in an invalid path
        return False
    else:
        # Special case where we're skipping index 1. We've already set inc and
        # that might cause a problem if the list is decreasing but only the
        # first two elements are increasing or vice-versa.
        # Example: [7, 9, 6, 5, 4]
        
        if safe == False:
            # We have to skip
            if curr_idx == 1:
                return backtrack(l, prev_idx, curr_idx + 1, violations + 1, None)
            else:
                return backtrack(l, prev_idx, curr_idx + 1, violations + 1, inc)
        else:
            # Try both paths where we either skip or don't skip
            if curr_idx == 1:
                return backtrack(l, curr_idx, curr_idx + 1, violations, inc) or \
                        backtrack(l, prev_idx, curr_idx + 1, violations + 1, None)
            else:
                return backtrack(l, curr_idx, curr_idx + 1, violations, inc) or \
                    backtrack(l, prev_idx, curr_idx + 1, violations + 1, inc)

def main():
    f = open("./input.txt", "r")

    ans = 0
    for line in f:
        l = line.split()

        violations = 0
        inc = None
        safe = False
        for i in range(len(l)):
            l[i] = int(l[i])

        if backtrack(l, None, 0, 0, None):
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()