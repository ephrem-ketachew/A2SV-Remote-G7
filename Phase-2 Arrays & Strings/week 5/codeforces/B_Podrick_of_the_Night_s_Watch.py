# B. Podrick of the Night's Watch
# time limit per test1 second
# memory limit per test256 megabytes

# In the ancient days of the Seven Kingdoms, ravens were the only means by which men could send their words across the realm — to friends, to foes, and sometimes... to ladies.

# Among the brothers of the Night's Watch, it is forbidden for a man to love or court any woman while he serves the Watch. Yet Ahmed and Kidus, two brothers of the order, began to suspect their fellow brother Mikias. They asked him whether he was speaking to a lady, but he denied it. Still, they were not convinced, and they knew they must uncover the truth on their own before making such a grave accusation. They even began to fear that Mikias might become Podrick of the Night's Watch.

# No man can follow a raven once it takes flight, nor read the secrets it carries. Thus, Ahmed and Kidus chose another path.

# They gathered records of Mikias's ravens over n
#  days. For each day, they recorded the hour h
#  at which each raven was sent (in 24
# -hour format, using only the hour h
#  where 0≤h<24
# ), and the name s
#  of the raven that carried the message.

# After long thought, they agreed upon the following belief:

# If Mikias sends a raven with the same name at the same hour in at least 80%
#  of the days, then surely this raven carries messages to a lady.
# Define the Raven Consistency Ratio (RCR) as:
# RCR=(number of days in which the same (name, hour) appears/total number of days)×100

# If the RCR
#  is at least 80%
# , the raven is considered suspicious.

# Your task is to determine whether Mikias is secretly sending ravens to a lady; in other words, determine whether there exists a pair (s,h)
#  whose RCR
#  is at least 80%
# .

# It is guaranteed that within the same day, the same pair (s,h)
#  does not appear more than once.

# Input
# The first line contains an integer n
#  (5≤n≤104)
#  — the number of days.

# For each day:

# The first line contains an integer m
#  (1≤m≤2×104)
#  — the number of messages sent on that day.

# Each of the next m
#  lines contains a string s
#  consists only of lowercase English letters (1≤|s|≤30)
#  and an integer h
#  (0≤h<24)
#  — the name of the raven and the hour at which it was sent.

# It is guaranteed that the sum of all values of m
#  over all days does not exceed 2×105
# .

# Output
# Print "YES" if there exists a pair (s,h)
#  such that Mikias sent that raven at that exact hour in at least 80%
#  of the days. Otherwise, print "NO".

# The output is case-insensitive: any combination of uppercase and lowercase letters for "yes" or "no" will be accepted.

# Examples
# InputCopy
# 5
# 4
# nightwing 0
# frostwing 5
# kingfeather 10
# moonfeather 23
# 4
# nightwing 0
# frostwing 5
# kingfeather 10
# moonfeather 23
# 4
# nightwing 0
# frostwing 5
# kingfeather 10
# moonfeather 23
# 1
# frostwing 5
# 1
# frostwing 5
# OutputCopy
# YES
# InputCopy
# 5
# 3
# shadowclaw 2
# ghostfeather 3
# starwing 4
# 3
# shadowclaw 4
# shadowclaw 23
# starwing 23
# 2
# ghostfeather 5
# starwing 6
# 3
# shadowclaw 23
# ghostfeather 23
# starwing 23
# 2
# shadowclaw 1
# starwing 2
# OutputCopy
# NO

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

sh_pairs = Counter()

for _ in range(n):
    m = int(input())
    for _ in range(m):
        s, h = input().split()
        h = int(h)
        
        sh_pairs[(s, h)] += 1
        
is_suspicious = False
for pair in sh_pairs:
    rcr = sh_pairs[pair] / n
    if rcr >= 0.8:
        is_suspicious = True
        
if is_suspicious:
    print('YES')
else:
    print('NO')