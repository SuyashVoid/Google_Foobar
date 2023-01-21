# This solution is O(n) with n being the number of the digits in the number. It only takes O(1) time to find practically
# since the number of digits in the number is limited to 309.
def solution(n):
    binaryStr = decStrToBinStr(n)
    binary = list(binaryStr)
    length = len(binary)
    iterator = len(binary) - 1  # Start at the end of the binary string
    additions = 0  # Any sequence of 1s will be taken care of by adding 1
    subtracts = 0  # Any 1 not part of a sequence will be taken care of by subtracting 1
    halves = 0  # Whole length of string after adds and subs will be taken care of by halving
    # print(binary)
    if n == "1":
        return 0
    while iterator >= 0:
        ones = 0
        while binary[iterator] == '1' and iterator >= 0:  # Count the number of 1s in a row
            ones += 1
            iterator -= 1  # Move to the next digit (left)

        if ones == 1 and iterator > 0:  # If there is only one 1, we would have subtracted here
            subtracts += 1
        if ones > 1:  # If there is more than one 1, we would have added here
            # special case for 3
            if iterator < 0 and ones == 2:  # Special case for 3 when subtracting is fewer steps than adding
                subtracts += 1
                halves -= 1
            else:
                additions += 1  # Add 1 to the number of additions
                binary[iterator] = '1'  # Set the next digit to 1
                iterator += 1  # Move to the next digit (right)
        iterator -= 1

    if binary[1] == '1':
        halves = halves + length
    else:
        halves = halves + length - 1
    # print(binary)
    return halves + subtracts + additions


# https://stackoverflow.com/questions/11006844/convert-a-very-large-number-from-decimal-string-to-binary-representation
# Big decimal string to binary string without using any unsigned integer types by paxdiablo (Jun 13, 2012)
def decStrToBinStr(num):
    if num == '0':
        stack = '0'
    else:
        stack = ''
        while num != '0':
            stack = '%d%s' % (oddsToOne(num), stack)
            num = divByTwo(num)
    return stack


def divByTwo(s):
    new_s = ''
    add = 0

    for ch in s:
        new_dgt = (ord(ch) - ord('0')) // 2 + add
        new_s = '%s%d' % (new_s, new_dgt)
        add = oddsToOne(ch) * 5

    if new_s != '0' and new_s.startswith('0'):
        new_s = new_s[1:]

    return new_s


def oddsToOne(s):
    if s.endswith('1'): return 1
    if s.endswith('3'): return 1
    if s.endswith('5'): return 1
    if s.endswith('7'): return 1
    if s.endswith('9'): return 1
    return 0


if __name__ == '__main__':
    print(solution(str(10 ** 1000)))
    # print(solution(str(4)))
    # halver(344)
