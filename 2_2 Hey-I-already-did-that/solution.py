# This solution is O(n) time as I use a set which is expected to be O(1) lookup time and we simply .
def solution(n, b):
    setOfIds = set()
    setOfIds.add(n)
    cycleStarted = 0  # This is a flag to indicate if we have started a cycle and also used to check
    # if we are going through elements of a cycle a second time.
    toStopAt = ""       # This is the element we will stop at when we are going through a cycle a second time.
    streak = 0          # This is the length of the cycle.
    nextIdentity = nextID(n, b)
    while True:
        if nextIdentity not in setOfIds:
            setOfIds.add(nextIdentity)
            cycleStarted = 0    # If an element is not in the set, we were never in a cycle (so no streak either).
            streak = 0
        else:
            if cycleStarted > 0 and nextIdentity == toStopAt:   # If we are in a cycle and we are seeing the start a
                # second time, this is the end of the cycle.
                streak += 1
                break
            if cycleStarted == 0:                    # If we were not in cycle, then we are probably starting one.
                toStopAt = nextIdentity
                cycleStarted += 1
            else:
                streak += 1                          # If we are in a cycle and more elements are alredy in the set,
                # increment the streak.
        nextIdentity = nextID(nextIdentity, b)      # Get the next identity.
    return streak


# This function figures out the next identity.
def nextID(n, b):
    yMid = sorted(n)
    xMid = sorted(n, reverse=True)
    k = len(n)
    x = int("".join(xMid), b)
    y = int("".join(yMid), b)
    diff = numberToBase((x - y), b)
    return ''.join(map(str, diff)).zfill(k)


# This function converts a number to a base b.
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


if __name__ == '__main__':
    n = "210022"
    b = 3
    print(solution(n, b))
