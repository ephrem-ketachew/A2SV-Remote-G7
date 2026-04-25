import sys 

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, c = input().split()
    s = input().strip()
    n = int(n)
    
    if c == 'g':
        print(0)
        continue
    
    min_wait = 0
    s = s * 2
    prev = -1
    for i, ch in enumerate(s):
        if i >= n and prev == -1:
            break
        
        if ch == 'g':
            if prev != -1:
                min_wait = max(min_wait, i - prev)
                prev = -1
        elif ch == c:
            if prev == -1:
                prev = i
                
    print(min_wait)