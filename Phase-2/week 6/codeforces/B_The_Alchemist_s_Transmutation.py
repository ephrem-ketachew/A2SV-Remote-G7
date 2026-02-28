import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    
    if min(arr) <= x <= max(arr):
        output.append('YES')
    else:
        output.append('NO')
        
print('\n'.join(output))