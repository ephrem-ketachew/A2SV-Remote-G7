# A left rotation operation on a circular array shifts each of the array's elements 1 unit to the left. The elements that fall off the left end reappear at
# the right end. Given an integer d, rotate the array that many steps to the left and return the result.

# Example

# d=2

# arr = [1,2, 3, 4, 5]

# After 2 rotations, arr' = [3, 4, 5, 1, 2].

# Function Description

# Complete the rotateLe ft function with the following parameters:

# . int d: the amount to rotate by

# . int arr[n]: the array to rotate

# Returns

# . int[n]: the rotated array

# Input Format

# The first line contains two space-separated integers that denote n, the number of integers, and d, the number of left rotations to perform.
# The second line contains n space-separated integers that describe arr].

# Constraints

# . 1 ≤ n ≤ 105
# . 1≤d ≤n
# · 1 ≤ ali] ≤ 106

# Sample Input

# STDIN

# Function
# 54
# 1 2 3 4 5 arr = [1, 2, 3, 4, 5]

# n = 5 d = 4

# Sample Output

# 51234

# Explanation

# To perform d = 4 left rotations, the array undergoes the following sequence of changes:

# [1,2,3,4,5]>[2,3,4,5,1]>[3,4,5,1,2]>[4,5,1,2,3]> [5,1,2,3,4]

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    return arr[d:] + arr[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
