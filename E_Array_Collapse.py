# E. Array Collapse
# time limit per test2 s.
# memory limit per test256 MB
# You are given an array a
#  of length n
# , a positive integer m
# , and a string of commands of length n
# . Each command is either the character 'L' or the character 'R'.

# Process all n
#  commands in the order they are written in the string s
# . Processing a command is done as follows:

# First, output the remainder of the product of all elements of the array a
#  when divided by m
# .
# Then, if the command is 'L', remove the leftmost element from the array a
# , if the command is 'R', remove the rightmost element from the array a
# .
# Note that after each move, the length of the array a
#  decreases by 1
# , and after processing all commands, it will be empty.

# Write a program that will process all commands in the order they are written in the string s
#  (from left to right).

# Input
# The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases in the input. Then descriptions of t
#  test cases follow.

# Each test case of the input is given by three lines.

# The first line contains two integers n
#  and m
#  (1≤n≤2⋅105,1≤m≤104
# ) — the initial length of the array a
#  and the value to take the remainder by.

# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤104
# ) — the elements of the array a
# .

# The third line contains a string s
#  consisting of n
#  characters 'L' and 'R'.

# It is guaranteed that the sum of the values of n
#  for all test cases in a test does not exceed 2⋅105
# .

# Output
# For each test case, output n
#  integers b1,b2,…,bn
# , where bi
#  is the remainder when dividing the product of all elements of the current state of the array a
#  by m
#  at the beginning of the execution of the i
# -th command.

# Example
# InputCopy
# 4
# 4 6
# 3 1 4 2
# LRRL
# 5 1
# 1 1 1 1 1
# LLLLL
# 6 8
# 1 2 3 4 5 6
# RLLLRR
# 1 10000
# 10000
# R
# OutputCopy
# 0 2 4 1 
# 0 0 0 0 0 
# 0 0 0 4 4 4 
# 0 
# Note
# In the first test case of the example:

# 3⋅1⋅4⋅2mod6=24mod6=0
# ;
# s1=L
# , so we remove the first element and get the array [1,4,2]
# ;
# 1⋅4⋅2mod6=8mod6=2
# ;
# s2=R
# , so we remove the last element and get the array [1,4]
# ;
# 1⋅4mod6=4mod6=4
# ;
# s3=R
# , so we remove the last element and get the array [1]
# ;
# 1mod6=1
# ;
# s4=L
# , so we remove the first element and get an empty array.

import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input().strip()
    
    order = []
    left, right = 0, n - 1
    for cmd in s:
        if cmd == 'L':
            order.append(a[left])
            left += 1
        else:
            order.append(a[right])
            right -= 1
            
    order.reverse()
    ans = []
    pdt = 1
    for num in order:
        pdt = (pdt * num) % m
        ans.append(str(pdt))
        
    ans.reverse()
    
    output.append(' '.join(ans))
    
print('\n'.join(output))