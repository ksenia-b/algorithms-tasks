#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    a = m // n
    result  = ( m // n + s - 1) // n

    if not result:
        return n
    return result




# def calculate(first_value, n):
#     count_times = first_value // n
#
#     if n // first_value + s - 1 == 0:
#         return n
#     return  first_value - count_times * n



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # t = int(input().strip())
    #
    # for t_itr in range(t):
    #     first_multiple_input = input().rstrip().split()
    #
    #     n = int(first_multiple_input[0])
    #
    #     m = int(first_multiple_input[1])
    #
    #     s = int(first_multiple_input[2])
    n = 7
    m = 615562705
    s = 2
    result = saveThePrisoner(n, m, s)
    print("result = ", abs(result))
    # pass
    #
    # lines = []
    # with open('input.txt') as f:
    #     lines = f.readlines()
    #
    # with open('output.txt') as f:
    #     lines_output = f.readlines()
    #
    #
    # count = 0
    # for line in lines:
    #     count += 1
    #     print(f'line {count}: {line}')
    #     line = line.split(' ')
    #     n = int(line[0])
    #     m = int(line[1])
    #     s = int(line[2])
    #
    #
    #     result = saveThePrisoner(n, m, s)
    #     print("result = ", abs(result))
    #     if result == int(lines_output[count]):
    #
    #         continue
    #     else:
    #         print('not equial, line = ', line, "output = ", lines_output[count])
    #
    #
