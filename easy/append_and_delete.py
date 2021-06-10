# hackerhappy
# hackerrank
# 9

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    for item in s:

        if len(t) > count and item == t[count]:
            count += 1
            continue

    new_s = len(s) - count
    new_t = len(t) - count

    if (new_s + new_t) <= k:
        if (len(t) + len(s) <= k):
            return "Yes"

        elif ((k - (new_s + new_t)) % 2 == 0):
            return "Yes"

        else:
            return "No"
    return "No"


# if (k == count  or k >= new_s + new_t):
    #     if (new_s + new_t) % k != 0:
    #         return "False"
    #     return "Yes";
    # elif ((new_s + new_t) % k == 0 and count <= k):
    #     return "Yes";
    # else:
    #     return "No"
    # if (new_s + new_t) % k:
    #     result = 'Yes'

    # elif new_s + new_t <= k :
    #     if (new_s + new_t) % k == 0:
    #         result = 'Yes'
    #
    #     if len(s) < len(t):
    #         if len(s) + len(t) > k:
    #             result = 'No'
    # else:
    #     result = 'No'


    # print("result = ", result)




if __name__ == '__main__':


    # s = input()
    #
    # t = input()
    #
    # k = int(input().strip())
    s = 'qwerasdf'
    t = 'qwerbsdf'
    k = 6

    result = appendAndDelete(s, t, k)

