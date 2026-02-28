import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    min_op = float('inf')
    for i in range(1, n - 1):
        op = (arr[i] - arr[i - 1]) + (arr[i + 1] - arr[i])
        min_op = min(min_op, op)
       
    output.append(str(min_op))
    
print('\n'.join(output))