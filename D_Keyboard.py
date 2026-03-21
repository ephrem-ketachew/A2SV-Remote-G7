import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    s = input().strip()
    n = len(s)
    
    functioning_chars = set()
    i = 0
    while i < n:
        ch = s[i]
        count = 0
        while i < n and s[i] == ch:
            count += 1
            i += 1
            
        if count % 2 == 1:
            functioning_chars.add(ch)
    
    ans = sorted(functioning_chars)
    
    output.append(''.join(ans))
    
print('\n'.join(output))