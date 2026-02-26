# Sorting
# One common task for computers is to sort data. For example, people might want to see all their files on a computer sorted by size. Since sorting is a simple problem with many different possible solutions, it is often used to introduce the study of algorithms.

# Insertion Sort
# These challenges will cover Insertion Sort, a simple and intuitive sorting algorithm. We will first start with a nearly sorted list.

# Insert element into sorted list
# Given a sorted list with an unsorted number  in the rightmost cell, can you write some simple code to insert  into the array so that it remains sorted?

# Since this is a learning exercise, it won't be the most efficient way of performing the insertion. It will instead demonstrate the brute-force method in detail.

# Assume you are given the array  indexed . Store the value of . Now test lower index values successively from  to  until you reach a value that is lower than , at  in this case. Each time your test fails, copy the value at the lower index to the current index and print your array. When the next lower indexed value is smaller than , insert the stored value at the current index and print the entire array.

# Example


# Start at the rightmost index. Store the value of . Compare this to each element to the left until a smaller value is reached. Here are the results as described:

# 1 2 4 5 5
# 1 2 4 4 5
# 1 2 3 4 5
# Function Description

# Complete the insertionSort1 function in the editor below.

# insertionSort1 has the following parameter(s):

# n: an integer, the size of 
# arr: an array of integers to sort
# Returns

# None: Print the interim and final arrays, each on a new line. No return value is expected.
# Input Format

# The first line contains the integer , the size of the array .
# The next line contains  space-separated integers .

# Constraints



# Output Format

# Print the array as a row of space-separated integers each time there is a shift or insertion.

# Sample Input

# 5
# 2 4 6 8 3
# Sample Output

# 2 4 6 8 8 
# 2 4 6 6 8 
# 2 4 4 6 8 
# 2 3 4 6 8 
# Explanation

#  is removed from the end of the array.
# In the st line , so  is shifted one cell to the right.
# In the nd line , so  is shifted one cell to the right.
# In the rd line , so  is shifted one cell to the right.
# In the th line , so  is placed at position .

# Next Challenge

# In the next Challenge, we will complete the insertion sort.

# Language
# Python 3
# More
# 1234567891011121314151617181920212223242526
# #
# # The function accepts following parameters:
# #  1. INTEGER n
# #  2. INTEGER_ARRAY arr
# #

# def insertionSort1(n, arr):
#     # Write your code here

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     insertionSort1(n, arr)

# Line: 14 Col: 10

# Test against custom input
# AuthorHackerRank
# DifficultyEasy
# Max Score30
# Submitted By232027
# Need Help?
# View discussions
# View top submissions
# rate this challenge

# MORE DETAILS
# Download problem statement
# Download sample test cases
# Suggest Edits
# Share on FacebookShare on TwitterShare on LinkedIn

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    arr = [str(num) for num in arr]
    i = len(arr) - 2
    key = arr[-1]
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i -= 1
        print(' '.join(arr))
    arr[i + 1] = key
    print(' '.join(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
