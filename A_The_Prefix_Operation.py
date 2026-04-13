# A. The Prefix Operation
# time limit per test1 s.
# memory limit per test256 MB
# Milica has a string s
#  of length n
# , consisting only of characters A and B. She wants to modify s
#  so it contains exactly k
#  instances of B. In one operation, she can do the following:

# Select an integer i
#  (1≤i≤n
# ) and a character c
#  (c
#  is equal to either A or B).
# Then, replace each of the first i
#  characters of string s
#  (that is, characters s1,s2,…,si
# ) with c
# .
# Milica does not want to perform too many operations in order not to waste too much time on them.

# She asks you to find the minimum number of operations required to modify s
#  so it contains exactly k
#  instances of B. She also wants you to find these operations (that is, integer i
#  and character c
#  selected in each operation).

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of test cases follows.

# The first line of each test case contains two integers n
#  and k
#  (3≤n≤100
# , 0≤k≤n
# ) — the length of the string s
#  and the number of characters B Milica wants to appear in s
#  in the end.

# The second line of each test case contains the string s
#  of length n
# , consisting only of characters A and B.

# Output
# For each test case, in the first line output a single integer m
#  — the minimum number of operations Milica should perform.

# In the j
# -th of the next m
#  lines output an integer i
#  (1≤i≤n
# ) and a character c
#  (c
#  is 'A' or 'B') — the parameters of the j
# -th operation as described in the statement.

# If there are multiple solutions with the minimum possible number of operations, output any of them.

# Example
# InputCopy
# 5
# 5 2
# AAABB
# 5 3
# AABAB
# 5 0
# BBBBB
# 3 0
# BAA
# 10 3
# BBBABBBBAB
# OutputCopy
# 0
# 1
# 1 B
# 1
# 5 A
# 1
# 2 A
# 1
# 6 A
# Note
# In the first test case, there are already 2
#  characters B in s
# , so Milica does not have to perform any operations.

# In the second test case, the only way to achieve 3
#  characters B in s
#  in one operation is to replace the first character of s
#  by B on the first operation: AABAB →
#  BABAB.

# In the third test case, the only way to achieve 0
#  characters B in s
#  in one operation is to replace the first 5
#  characters of s
#  by A on the first operation: BBBBB →
#  AAAAA.

# In the fourth test case, one of the ways to achieve 0
#  characters B in s
#  in one operation is to replace the first 2
#  characters of s
#  by A on the first operation: BAA →
#  AAA. Note that "1 A" and "3 A" are also correct one-operation solutions.

import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    b = s.count('B')
    if b == k:
        output.append('0')
        continue
    
    output.append('1')
    if b > k:
        i = n - 1
        count = 0
        while count < k:
            if s[i] == 'B':
                count += 1
            i -= 1
            
        output.append(f'{i + 1} A')
        
    else:
        count = b
        i = 0
        while count < k:
            if s[i] == 'A':
                count += 1
            i += 1
            
        output.append(f'{i} B')
        
print('\n'.join(output))