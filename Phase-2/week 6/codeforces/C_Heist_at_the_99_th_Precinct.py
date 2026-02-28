import sys

input = sys.stdin.readline

t = int(input())

output = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    
    win = False
    i = 0
    while i < n:
        count = 0
        num = arr[i]
        while i < n and arr[i] == num:
            i += 1
            count += 1
            
        if count % 2 == 1:
            win = True
            break
    
    if win:
        output.append('YES')
    else:
        output.append('NO')
        
print('\n'.join(output))