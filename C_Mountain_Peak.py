import sys 

input = sys.stdin.readline

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    
    prefix = [0] * n
    min_val = h[0]
    min_idx = 0
    for i in range(n):
        if h[i] < min_val:
            min_idx = i
            min_val = h[i]
        prefix[i] = (min_val, min_idx)
        
    suffix = [0] * n
    min_val = h[-1]
    min_idx = n - 1
    for i in range(n - 1, -1, -1):
        if h[i] < min_val:
            min_idx = i
            min_val = h[i]
        suffix[i] = (min_val, min_idx)
        
    exists = False
    ans = []
    for i in range(1, n - 1):
        if prefix[i - 1][0] < h[i] and h[i] > suffix[i + 1][0]:
            exists = True
            ans = [str(prefix[i - 1][1] + 1), str(i + 1), str(suffix[i + 1][1] + 1)]
            break
            
    if exists:
        output.append('YES')
        output.append(' '.join(ans))
    else:
        output.append('NO')

        
print('\n'.join(output))
    