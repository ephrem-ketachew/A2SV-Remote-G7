# C. Ghadeer and the Royal Decrees
# time limit per test1 s.
# memory limit per test256 MB

# In the ancient days of the Seven Kingdoms, when the Iron Throne governed the realm through royal decrees and shifting balances of power, even the strength of noble houses could rise or fall with a single command from the crown.

# After receiving yet another integer array a1,a2,…,an
#  during the Grand Feast at Winterfell, Lady Ghadeer of House Index decides to perform some royal decrees upon it.

# Formally, there are m
#  operations that she is going to perform in order. Each of them belongs to one of the two types:

# + l r
# . Given two integers l
#  and r
# , for all 1≤i≤n
#  such that l≤ai≤r
# , set ai:=ai+1
# .
# - l r
# . Given two integers l
#  and r
# , for all 1≤i≤n
#  such that l≤ai≤r
# , set ai:=ai−1
# .
# In the realm, this means that every house whose strength lies between l
#  and r
#  either gains one soldier (for +
# ) or loses one soldier (for -
# ).

# For example, if the initial array a=[7,1,3,4,3]
# , after performing the operation + 2 4
# , the array a=[7,1,4,5,4]
# . Then, after performing the operation - 1 10
# , the array a=[6,0,3,4,3]
# .

# Napoleon Jr., Master of Coin, is curious about the maximum value in the array a
# . Help him find it after each of the m
#  operations.

# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤2⋅104
# ) — the number of test cases. The description of the test cases follows.

# The first line of each test case contains two integers n
#  and m
#  (1≤n≤105
# , 1≤m≤105
# ) — the length of the array and the number of operations.

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the initial array a
# .

# Then m
#  lines follow, each line corresponds to the operation, in the following format: c l r
#  (c∈{+,-}
# , l
#  and r
#  are integers, 1≤l≤r≤109
# ) — the description of the operation.

# Note that the elements ai
#  may not satisfy 1≤ai≤109
#  after some operations, as shown in the example.

# It is guaranteed that the sum of n
#  over all test cases does not exceed 105
# , and the sum of m
#  over all test cases does not exceed 105
# .

# Output
# For each test case, output one single line containing m
#  integers, with the i
# -th of them describing the maximum value of the array after the i
# -th operation.

# Example
# InputCopy
# 5
# 5 5
# 1 2 3 2 1
# + 1 3
# - 2 3
# + 1 2
# + 2 4
# - 6 8
# 5 5
# 1 3 3 4 5
# + 1 4
# + 2 3
# - 4 5
# - 3 3
# - 2 6
# 5 5
# 1 1 1 1 1
# + 2 3
# - 4 5
# + 1 6
# - 2 5
# + 1 8
# 1 1
# 1
# - 1 1
# 1 1
# 1000000000
# + 1000000000 1000000000
# OutputCopy
# 4 4 4 5 5
# 5 5 4 4 3
# 1 1 2 1 2
# 0
# 1000000001
# Note
# In the first test case, the process of the operations is listed below:

# After the first operation, the array becomes equal to [2,3,4,3,2]
# . The maximum value is 4
# .
# After the second operation, the array becomes equal to [1,2,4,2,1]
# . The maximum value is 4
# .
# After the third operation, the array becomes equal to [2,3,4,3,2]
# . The maximum value is 4
# .
# After the fourth operation, the array becomes equal to [3,4,5,4,3]
# . The maximum value is 5
# .
# After the fifth operation, the array becomes equal to [3,4,5,4,3]
# . The maximum value is 5
# .
# In the second test case, the process of the operations is listed below:

# After the first operation, the array becomes equal to [2,4,4,5,5]
# . The maximum value is 5
# .
# After the second operation, the array becomes equal to [3,4,4,5,5]
# . The maximum value is 5
# .
# After the third operation, the array becomes equal to [3,3,3,4,4]
# . The maximum value is 4
# .
# After the fourth operation, the array becomes equal to [2,2,2,4,4]
# . The maximum value is 4
# .
# After the fifth operation, the array becomes equal to [1,1,1,3,3]
# . The maximum value is 3
# .

import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans = []
    maxx = max(arr)
    for _ in range(m):
        c, l, r = input().split()
        l, r = int(l), int(r)
        
        if l <= maxx <= r:
            if c == '+':
                maxx += 1
            else:
                maxx -= 1
                
        ans.append(str(maxx))
        
    output.append(' '.join(ans))
    
print('\n'.join(output))
        