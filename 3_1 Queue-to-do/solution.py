# This solution is O(n) with n being the length of the lines minion get in for. It only takes O(1) time to find the
# XOR for each iteration of line.
def solution(start, length):
    idEdges = idListFinder(start, length)
    finalChecksum = 0
    for i in range(len(idEdges)):
        finalChecksum ^= computeXORRange(idEdges[i][0], idEdges[i][1])
    return finalChecksum


# Finds the start and end points (range) to find XOR for
def idListFinder(start, length):
    ranges = []
    matrixDimension = length
    while length > 0:
        ranges.append((start, start + length - 1))
        start += length + (matrixDimension - length)
        length -= 1
    return ranges


# XOR from a to b using fast XOR
def computeXORRange(a, b):
    # This identity follows from basic properties of XOR
    return computeXOR(a - 1) ^ computeXOR(b)


# XOR from 1 to n from GeeksForGeeks
def computeXOR(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0


if __name__ == '__main__':
    print(solution(17, 4))
