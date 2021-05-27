#!/bin/python3
# hackerrank link: https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(house, trees, apples, oranges):
    # Write your code here

    count_apples = 0
    count_oranges = 0

    # Write your code here
    # for apple in apples:
    #     apple += a
    #     if apple >= s and apple <= t:
    #         count_apples += 1
    #
    # for orange in oranges:
    #     orange += b
    #     if orange >= s and orange <= t:
    #         count_oranges += 1
    #
    # print(count_apples)
    # print(count_oranges)
    #
    print(sum([1 for apple in apples if (x + a) >= s and (x + a) <= t]))
    print(sum(1 for orange in oranges if (x + b) >= s and (x + b) <= t ))






if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    # countApplesAndOranges(s, t, a, b, apples, oranges)
    countApplesAndOranges([7, 10], [4, 12], [2, 3, -4], [3, -4, -4])
