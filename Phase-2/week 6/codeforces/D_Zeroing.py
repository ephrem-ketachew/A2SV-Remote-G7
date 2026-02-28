import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

output = []

arr.sort()
dec = 0
i = 0
for _ in range(k):
    while i < n and arr[i] - dec == 0:
        i += 1
    if i < n:
        output.append(str(arr[i] - dec))
        dec += arr[i] - dec
    else:
        output.append('0')
        
print('\n'.join(output))