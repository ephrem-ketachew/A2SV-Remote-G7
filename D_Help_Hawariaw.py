# D. Help Hawariaw
# time limit per test2 s.
# memory limit per test256 MB
# A progressive square of size n
#  is an n×n
#  matrix. Hawariaw chooses three integers a1,1
# , c
# , and d
#  and constructs a progressive square according to the following rules:

# ai+1,j=ai,j+c

# ai,j+1=ai,j+d

# For example, if n=3
# , a1,1=1
# , c=2
# , and d=3
# , then the progressive square looks as follows:

# ⎛⎝⎜1354687911⎞⎠⎟

# Last month Hawariaw constructed a progressive square and remembered the values of n
# , c
# , and d
# . Recently, he found an array b
#  of n2
#  integers in random order and wants to make sure that these elements are the elements of that specific square.

# It can be shown that for any values of n
# , a1,1
# , c
# , and d
# , there exists exactly one progressive square that satisfies all the rules.

# Input
# The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases.

# The first line of each test case contains three integers n
# , c
# , and d
#  (2≤n≤500
# , 1≤c,d≤106
# ) — the size of the square and the values of c
#  and d
#  as described in the statement.

# The second line of each test case contains n⋅n
#  integers b1,b2,…,bn⋅n
#  (1≤bi≤109
# ) — the elements found by Maxim.

# It is guaranteed that the sum of n2
#  over all test cases does not exceed 25⋅104
# .

# Output
# For each test case, output "YES" in a separate line if a progressive square for the given n
# , c
# , and d
#  can be constructed from the array elements a
# , otherwise output "NO".

# You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.

# Example
# InputCopy
# 5
# 3 2 3
# 3 9 6 5 7 1 10 4 8
# 3 2 3
# 3 9 6 5 7 1 11 4 8
# 2 100 100
# 400 300 400 500
# 3 2 3
# 3 9 6 6 5 1 11 4 8
# 4 4 4
# 15 27 7 19 23 23 11 15 7 3 19 23 11 15 11 15
# OutputCopy
# NO
# YES
# YES
# NO
# NO

import sys 
from collections import Counter

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, c, d = map(int, input().split())
    b = list(map(int, input().split()))
    
    counter = Counter(b)
    
    possible = True
    start = min(b)
    for _ in range(n):
        cur = start - d
        for i in range(n):
            cur += d
            if counter[cur] == 0:
                possible = False
                break
            counter[cur] -= 1
        
        if not possible:
            break
        
        start += c
        
    if possible:
        output.append('YES')
    else:
        output.append('NO')
        
print('\n'.join(output))