import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    p = [0] * n
    left = right = 0
    possible = True
    while right < n:
        num = s[right]
        left = right
        while right < n and s[right] == num:
            right += 1
            
        if right - left == 1:
            output.append('-1')
            possible = False
            break
        
        for i in range(left, right - 1):
            p[i] = str(i + 2)
            
        p[right - 1] = str(left + 1)
        
    if possible:
        output.append(' '.join(p))
        
print('\n'.join(output))