import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        a = list(map(int, input().split()))
        arr.append(a)
        
    arr.sort(key=lambda a: a[0] + a[1])
    
    ans = []
    for a in arr:
        ans.append(str(a[0]))
        ans.append(str(a[1]))
        
    output.append(' '.join(ans))
    
print('\n'.join(output))