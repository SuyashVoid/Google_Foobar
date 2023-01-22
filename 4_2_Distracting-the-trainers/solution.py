# =====================
#
# The time for the mass escape has come, and you need to distract the bunny trainers so that the workers can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the trainers are fond of bananas. And gambling. And thumb wrestling.
#
# The bunny trainers, being bored, readily accept your suggestion to play the Banana Games.
#
# You will set up simultaneous thumb wrestling matches. In each match, two trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet all their bananas, and the other trainer will match the bet. The winner will receive all of the bet bananas. You don't pair off trainers with the same number of bananas (you will see why, shortly). You know enough trainer psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of trainers will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to supervising the bunny workers, and you don't want THAT to happen!
#
# For example, if the two trainers that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to training bunnies.
#
# How is all this useful to distract the bunny trainers? Notice that if the trainers had started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.
#
# Now your plan is clear. You must pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop!
#
# Write a function solution(banana_list) which, given a list of positive integers depicting the amount of bananas the each trainer starts with, returns the fewest possible number of bunny trainers that will be left to watch the workers. Element i of the list will be the number of bananas that trainer i (counting from 0) starts with.
#
# The number of trainers will be at least 1 and not more than 100, and the number of bananas each trainer starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Python cases --
# Input:
# solution.solution(1,1)
# Output:
#     2
#
# Input:
# solution.solution([1, 7, 3, 21, 13, 19])
# Output:
#     0
#
# -- Java cases --
# Input:
# solution.solution(1,1)
# Output:
#     2
#
# Input:
# Solution.solution([1, 7, 3, 21, 13, 19])
# Output:
#     0
def solution(banana_list):
    foundPartner = {}
    pairedInversed = set()
    pairedForward = set()
    banana_list.sort()
    for i in range(len(banana_list)):
        foundPartner[i] = set()
    for i in range(len(banana_list)):
        for j in range(len(banana_list)):
            if i != j:
                # Check if trainers at i and j can be paired
                if lifeCycleFinder(banana_list[i], banana_list[j], 50):
                    # If so, add each other to their respective sets
                    foundPartner[i].add(j)
                    foundPartner[j].add(i)

    # Get partner frequency for each trainer
    partnerFreq = [len(foundPartner[i]) for i in range(len(banana_list))]

    # Used this to get 'indices' of wrestlers when sorted by pairing frequency
    indices = [i[0] for i in sorted(enumerate(partnerFreq), key=lambda x: x[1])]

    # Tries to pair up the trainers for wrestling sorted simply by their count of bananas.
    for i in indices:
        if i not in pairedInversed:
            for j in reversed(indices):
                if j not in pairedInversed:
                    if j in foundPartner[i]:
                        pairedInversed.add(i)
                        pairedInversed.add(j)
                        break

    # Tries to pair up the trainers for wrestling sorted simply by their count of bananas.
    for i in range(len(banana_list)):
        if i not in pairedForward:
            for j in range(len(banana_list)):
                if j not in pairedForward:
                    if j in foundPartner[i]:
                        pairedForward.add(i)
                        pairedForward.add(j)
                        break

    return len(banana_list) - max(len(pairedInversed), len(pairedForward))


# This functions simply attempts to find if there's a loop or not in the life cycle of the two trainers using the
# provided method in question but applies a few optimizations to make it faster.
def lifeCycleFinder(a, b, times):
    if (a+b) % 2 != 0:
        return True
    valsAttained = set()
    valsAttained.add(a)
    valsAttained.add(b)
    for i in range(times):
        if a == b:
            return False
        c = min(a, b)
        if a < b:
            # This can reduce the number of steps needed to find the cycle by a lot
            x = findSteps(a, b)
            if (a - b > 4 or a + b > 4) and x>1:
                c = 2 ** x * c
                b = b - c + a
                a = c
            else:
                a += c
                b -= c
        else:
            x = findSteps(a, b)
            if (a - b > 4 or a + b > 4) and x>1:
                c = 2 ** x * c
                a = a - c + b
                b = c
            else:
                a -= c
                b += c
        if a in valsAttained and b in valsAttained:
            return True
        else:
            valsAttained.add(a)
            valsAttained.add(b)
    return True


# What this function does is find the number of times the 'lower' trainer can bet before it's bananas become greater
# than the 'higher' trainer's bananas, so we can just skip these redundant steps.
def findSteps(a, b):
    # Only use this fn if a+b/a-b is greater than 4
    # Also only if a>=2b
    # print("Finding steps for {a} and {b}".format(a=a,b=b))
    if b > a:
        a, b = b, a
    if a == 1:
        return 0
    return log2((a / b) - 1) - 1


# This is a faster way to find the log base 2 of a number
def log2(x):
    x=int(x)
    return x.bit_length() - 1
if __name__ == '__main__':


    # start_time = time.time()
    # print("Number of guards left to watch the prisoners = ", solution(banana_list=[1, 1]))
    # # # print("---", (time.time() - start_time)," seconds ---")
    # # start_time = time.time()
    print("Number of guards left to watch the prisoners = ", solution(banana_list=[1, 7, 3, 21, 13, 19]))
    # # # print("---", (time.time() - start_time)," seconds ---")
    # # start_time = time.time()
    # print("Number of guards left to watch the prisoners = ", solution(banana_list=[1, 7, 5, 3, 19, 13, 53, 61]))
    # # # print("---", (time.time() - start_time)," seconds ---")
    # # start_time = time.time()
    # print("Number of guards left to watch the prisoners = ", solution(banana_list=[1, 3, 3, 1, 5, 1]))
    # # # print("---", (time.time() - start_time)," seconds ---")
    # # start_time = time.time()
    # print("Number of guards left to watch the prisoners = ", solution(banana_list=[2 ** 30 - 1, 2 ** 30 - 3]))
    # # print("---", (time.time() - start_time)," seconds ---")