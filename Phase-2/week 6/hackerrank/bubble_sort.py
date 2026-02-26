# consider the following version of Bubble Sort:

# for (int i = 0; i < n; i++) {
    
#     for (int j = 0; j < n - 1; j++) {
#         // Swap adjacent elements if they are in decreasing order
#         if (a[j] > a[j + 1]) {
#             swap(a[j], a[j + 1]);
#         }
#     }
    
# }

# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

# Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
# First Element: firstElement, where  is the first element in the sorted array.
# Last Element: lastElement, where  is the last element in the sorted array.
# Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

# Example

# swap    a       
# 0       [6,4,1]
# 1       [4,6,1]
# 2       [4,1,6]
# 3       [1,4,6]
# The steps of the bubble sort are shown above. It took  swaps to sort the array. Output is:

# Array is sorted in 3 swaps.  
# First Element: 1  
# Last Element: 6  
# Function Description

# Complete the function countSwaps in the editor below.

# countSwaps has the following parameter(s):

# int a[n]: an array of integers to sort
# Prints

# Print the three lines required, then return. No return value is expected.

# Input Format

# The first line contains an integer, , the size of the array .
# The second line contains  space-separated integers .

# Constraints

# Output Format

# Sample Input 0

# STDIN   Function
# -----   --------
# 3       a[] size n = 3
# 1 2 3   a = [1, 2, 3]
# Sample Output 0

# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3
# Explanation 0
# The array is already sorted, so  swaps take place.

# Sample Input 1

# 3
# 3 2 1
# Sample Output 1

# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3
# Explanation 1
# The array is not sorted, and its initial values are: . The following  swaps take place:

# At this point the array is sorted and the three lines of output are printed to stdout.

# Language
# Python 3
# More
# 123456789101112131415161718192021222324

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    count_swap = 0
    for _ in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count_swap += 1
                
    return count_swap

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    swap_cnt = countSwaps(a)
    
    print(f'Array is sorted in {swap_cnt} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')