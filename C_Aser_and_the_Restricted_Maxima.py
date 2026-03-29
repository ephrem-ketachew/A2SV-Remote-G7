# C. Aser and the Restricted Maxima
# time limit per test1 s.
# memory limit per test256 MB

# Aser The Conqueror has recently integrated n
#  new warriors into his grand army. To maintain absolute control, he must assign each warrior a unique power rank from 1
#  to n
# . However, his advisors have flagged certain positions—marked as 1
#  in a sacred string s
# —as belonging to "Ambitious Officers." Aser knows that if an Ambitious Officer ever becomes the most powerful member of any local battalion of size k
#  or more, they might gain enough influence to attempt a coup. To secure his reign, he must arrange the ranks such that no Ambitious Officer is ever the highest-ranked individual in any battalion they are a part of.

# Formally, you are given a binary string∗
#  s
#  of length n
# , and an integer k
# .

# Aser The Conqueror wants to construct a permutation†
#  p
#  of length n
# , so that for each 1≤i≤n
# , where si=1
# , the following holds:

# For each interval [l,r]
#  (1≤l≤r≤n
# ) whose length is at least k
#  (i.e. r−l+1≥k
# ), if it covers position i
#  (i.e. l≤i≤r
# ), then the maximum element among pl,pl+1,…,pr
#  is not pi
# .
# Note that there are no such constraints on indices with si=0
# .

# You have to find such a permutation, or determine that such permutations do not exist.

# ∗
# A binary string is a string where each character is either 0
#  or 1
# .

# †
# A permutation of length n
#  is an array consisting of n
#  distinct integers from 1
#  to n
#  in arbitrary order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (2
#  appears twice in the array), and [1,3,4]
#  is also not a permutation (n=3
#  but there is 4
#  in the array).

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.

# The first line of each test case contains two integers n
#  and k
#  (1≤n≤2⋅105
# , 1≤k≤n
# ) — the length of s
#  and the integer in the statements.

# The second line contains the binary string s
#  of length n
#  (si=0
#  or 1
# ).

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case:

# If there is at least one possible permutation:
# Print "YES" in the first line of output;
# Then, print n
#  integers p1,p2,…,pn
#  (1≤pi≤n
# , all pi
# -s are distinct) in the second line — the permutation you constructed.
# Otherwise, print "NO" in the single line of output.
# You can output the tokens in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

# If there are multiple answers, you may output any of them.

# Example
# InputCopy
# 6
# 2 1
# 00
# 4 3
# 0010
# 5 2
# 11011
# 7 5
# 1111110
# 8 4
# 00101011
# 10 2
# 1000000010
# OutputCopy
# YES
# 1 2
# YES
# 1 4 3 2
# NO
# NO
# YES
# 6 5 2 3 4 8 1 7
# YES
# 1 2 3 4 5 6 7 9 8 10
# Note
# In the first test case, you can output an arbitrary permutation of length n=2
# , since all si
# -s are equal to 0
# .

# In the second test case, p=[1,4,3,2]
#  is a valid answer because:

# The only position where si=1
#  is i=3
# . There are three distinct intervals [l,r]
#  covering index 3
# , whose length is at least k=3
# : [1,3]
# , [1,4]
# , and [2,4]
# ;
# And, for each of the three intervals, the maximum element among pl,…,pr
#  should be p2=4
# , which is not equal to p3=3
# .

import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    if k == 1 and s.count('1') > 0:
        output.append('NO')
        continue
    
    count_ones = 0
    for i in range(k):
        if s[i] == '1':
            count_ones += 1
        
    if count_ones == k:
        output.append('NO')
        continue
    
    possible = True
    for i in range(k, n):
        if s[i - k] == '1':
            count_ones -= 1
        if s[i] == '1':
            count_ones += 1
            
        if count_ones == k:
            output.append('NO')
            possible = False
            break
        
    if not possible:
        continue
    
    output.append('YES')
    ans = ['0'] * n
    cur_int = 1
    for i in range(n):
        if s[i] == '1':
            ans[i] = str(cur_int)
            cur_int += 1
        
    for i in range(n):
        if s[i] == '0':
            ans[i] = str(cur_int)
            cur_int += 1
            
    output.append(' '.join(ans))
    
print('\n'.join(output))