import random
import time
import math


# This solution is O(n^2) with n being the length of the list given
def solution(l):
    res = 0
    for i in range(len(l)):
        cA = 0
        cB = 0
        if i != len(l) - 1:  # Save a few iterations by not checking the last element
            for j in range(i):  # Check factors in the numbers before i
                if l[i] % l[j] == 0:
                    cA += 1
        if cA != 0:  # Save time if there are no factors
            for k in range(i + 1, len(l)):  # Check multiples in the numbers after i
                if l[k] % l[i] == 0:
                    cB += 1
            res += cA * cB  # Factor * multiple = total number of triplets
    return res


if __name__ == '__main__':
    lstA = [1, 1, 1]
    lstB = [1, 2, 3, 4, 5, 6]
    lstC = [10, 20, 30, 40, 15, 60, 5]

    limitVal = 199
    limitCount = 2000
    lst = [random.randint(2, limitVal) // 2 for num in range(0, limitCount)]
    st = time.time()
    # print(solution(lstC))
    print(solution(lstB))
    et = time.time()
    elapsed = et - st
    print(elapsed)
