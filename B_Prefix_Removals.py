import sys 
from collections import Counter

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    s = input().strip()
    n = len(s)
    
    counter = Counter(s)
    cur_counter = Counter()
    i = 0
    while i < n:
        ch = s[i]
        cur_counter[ch] += 1
        if cur_counter[ch] >= counter[ch]:
            break
        
        i += 1
        
    output.append(s[i:])
    
print('\n'.join(output))