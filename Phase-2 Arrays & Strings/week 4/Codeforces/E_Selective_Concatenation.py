# E. Selective Concatenation
# time limit per test1 s.
# memory limit per test256 MB
# In the A2SV remote classroom, students are divided into exactly k study groups. However, only the even-numbered groups submit their work for evaluation. The submissions are merged in order, and the instructor checks how well they match the expected sequence starting from 1.

# You are given an array a
#  of length n
#  and an even integer k
#  (2≤k≤n
# ). You need to split the array a
#  into exactly k
#  non-empty subarrays†
#  such that each element of the array a
#  belongs to exactly one subarray.

# Next, all subarrays with even indices (second, fourth, …
# , k
# -th) are concatenated into a single array b
# . After that, 0
#  is added to the end of the array b
# .

# The cost of the array b
#  is defined as the minimum index i
#  such that bi≠i
# . For example, the cost of the array b=[1,2,4,5,0]
#  is 3
# , since b1=1
# , b2=2
# , and b3≠3
# . Determine the minimum cost of the array b
#  that can be obtained with an optimal partitioning of the array a
#  into subarrays.

# †
# An array x
#  is a subarray of an array y
#  if x
#  can be obtained from y
#  by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.

# The first line of each test case contains two integers n
#  and k
#  (2≤k≤n≤2⋅105
# , k
#  is even) — the length of the array a
#  and the number of subarrays.

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the elements of the array a
# .

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output a single integer — the minimum cost of the array b
#  that can be obtained.

# Example
# InputCopy
# 4
# 3 2
# 1 1 1
# 8 8
# 1 1 2 2 3 3 4 4
# 5 4
# 1 1 1 2 2
# 5 4
# 1 1 1000000000 2 2
# OutputCopy
# 2
# 5
# 2
# 1
# Note
# In the first test case, there are only two possible partitionings: [[1],[1,1]]
#  and [[1,1],[1]]
# . In either case, b1=1
# , and b2≠2
# , so the cost is 2
# .

# In the second test case, there is only one possible partitioning, where b=[1,2,3,4,0]
# , so the cost is 5
#  (b5=0≠5
# ).

# In the third test case, the following partitioning works: [[1],[1,1],[2],[2]]
# . Then b=[1,1,2,0]
# , and the cost is 2
# .

import sys
input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split())) + [0]
    
    if n == k:
        ans = n // 2 + 1
        for i in range(1, n, 2):
            if arr[i] != (i + 1) // 2:
                ans = (i + 1) // 2
                break
        output.append(str(ans))
        
    else:
        has_non_one = False
        for i in range(1, n - k + 2):
            if arr[i] != 1:
                has_non_one = True
                
        if has_non_one:
            output.append(str('1'))
        else:
            output.append(str('2'))
            
print('\n'.join(output))
            