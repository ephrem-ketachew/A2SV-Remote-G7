# E. The Competition is Fierce
# time limit per test2 s.
# memory limit per test256 MB
# Ephrem the Professor is an organizer of a G7 Practice Contest event. There are n
#  Groups in G7 Remote education numbered from 1
#  to n
# . Ephrem knows all competitive programmers in G7. There are n
#  students: the i
# -th student is enrolled at a Group ui
#  and has a programming skill si
# .

# Ephrem has to decide on the rules now. In particular, the number of members in the team.

# Polycarp knows that if he chooses the size of the team to be some integer k
# , each Group will send their k
#  strongest (with the highest programming skill s
# ) students in the first team, the next k
#  strongest students in the second team and so on. If there are fewer than k
#  students left, then the team can't be formed. Note that there might be Groups that send zero teams.

# The strength of the G7 is the total skill of the members of all present teams. If there are no teams present, then the strength is 0
# .

# Help Ephrem to find the strength of G7 for each choice of k
#  from 1
#  to n
# .

# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of testcases.

# The first line of each testcase contains a single integer n
#  (1≤n≤2⋅105
# ) — the number of Groups and the number of students.

# The second line of each testcase contains n
#  integers u1,u2,…,un
#  (1≤ui≤n
# ) — the Group the i
# -th student is enrolled at.

# The third line of each testcase contains n
#  integers s1,s2,…,sn
#  (1≤si≤109
# ) — the programming skill of the i
# -th student.

# The sum of n
#  over all testcases doesn't exceed 2⋅105
# .

# Output
# For each testcase print n
#  integers: the strength of G7  — the total skill of the members of the present teams — for each choice of team size k
# .

# Example
# InputCopy
# 4
# 7
# 1 2 1 2 1 2 1
# 6 8 3 1 5 1 5
# 10
# 1 1 1 2 2 2 2 3 3 3
# 3435 3014 2241 2233 2893 2102 2286 2175 1961 2567
# 6
# 3 3 3 3 3 3
# 5 9 6 7 9 7
# 1
# 1
# 3083
# OutputCopy
# 29 28 26 19 0 0 0 
# 24907 20705 22805 9514 0 0 0 0 0 0 
# 43 43 43 32 38 43 
# 3083 
# Note
# In the first testcase the teams from each Group for each k
#  are:

# k=1
# :
# Group 1
# : [6],[5],[5],[3]
# ;
# Group 2
# : [8],[1],[1]
# ;
# k=2
# :
# Group 1
# : [6,5],[5,3]
# ;
# Group 2
# : [8,1]
# ;
# k=3
# :
# Group 1
# : [6,5,5]
# ;
# Group 2
# : [8,1,1]
# ;
# k=4
# :
# Group 1
# : [6,5,5,3]
# ;

import sys 
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input().strip())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))
    
    groups = defaultdict(list)
    for group_num, skill in zip(u, s):
        groups[group_num].append(skill)
        
    g7 = []
    for group_num in groups:
        group = groups[group_num]
        group.sort()
        
        m = len(group)
        prefix = [0] * m
        prefix[0] = group[0]
        for i in range(1, m):
            prefix[i] = group[i] + prefix[i - 1]
            
        prefix.reverse()
        
        g7.append(prefix)
        
    ans = [0] * n
    for group in g7:
        m = len(group)
        for i in range(1, m + 1):
            q = m // i
            p = q * i
            
            ans[i - 1] += group[0] - (group[p] if p < m else 0)

        
    output.append(' '.join(str(val) for val in ans))
    
print('\n'.join(output))